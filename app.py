import time
import os
import socketio
from flask import Flask, jsonify, request, redirect
from flask import render_template, flash
from sqlalchemy import create_engine
import pandas as pd
from flask_socketio import SocketIO, emit
import model

UPLOAD_FOLDER = '/upload'  # 文件存放路径
conn = create_engine('mysql+pymysql://dodo:GCTAhTwrPPmJczcp@node1:3306/dodo?charset=utf8')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['CONN'] = conn

# socketio = SocketIO()
# socketio.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/import')
def imports():
    return render_template('import.html')


@app.route('/automl')
def automl():
    return render_template('automl.html')


@app.route('/alogrithms')
def alogrithms():
    # 看看你的
    return render_template('alogrithms.html')


@app.route('/getAlgStatus')
def getAlgStatus():
    return render_template('algstatus.html')


@app.route('/edit')
def edit():
    return render_template('edit.html')


@app.route('/getAlogrithms')
def getAlogrithms():
    df = pd.read_sql_query('select * from algorithms', app.config['CONN'])
    df = df.fillna(" ")
    df = df.apply(pd.to_numeric, errors='ignore')
    #in64无法序列化问题
    columns = df.columns.values.tolist()
    for i in columns:
        if df[i].dtypes == 'int64':
            df[i] = df[i].astype('float')
    n = df.shape[0]  # 行数
    data = []
    page = int(request.args.get('page'))
    limit = int(request.args.get('limit'))
    start = (page - 1) * limit
    end = page * limit
    for i in range(start, min(end, n)):
        row = dict()
        row['id'] = df.iloc[i][0]
        row['algorithm_name'] = df.iloc[i][1]
        row['algorithm_type'] = df.iloc[i][2]
        row['location'] = df.iloc[i][3]
        row['file_type'] = df.iloc[i][4]
        row['description'] = df.iloc[i][5]
        data.append(row)
    return jsonify({'code': 0, 'msg': '', "count": n, "data": data})


@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file:
        TYPE = {'.py': 'python', '.java': 'java'}
        file_type = TYPE[os.path.splitext(file.filename)[1]]
        location = os.getcwd() + app.config['UPLOAD_FOLDER'] + '\\' + file.filename
        file.save(location)  # 需要添加当前路径名在前
    return jsonify({'filename': file.filename, 'location': location, 'file_type': file_type})

'''
@app.route('/webs')
def webs():
    return render_template('websocket.html')


@socketio.on('connect',namespace='/test')
def give_response():
    time.sleep(5)
    emit('server_response',
                  {'data': [2, 2]},
                  namespace='/test')
    time.sleep(2)
    emit('server_response',
                  {'data': [3, 3]},
                  namespace='/test')
'''

if __name__ == '__main__':
    # socketio.run(app,debug=True,host='0.0.0.0',port=5000)
    app.run()
