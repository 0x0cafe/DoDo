import time

import socketio
from flask import Flask, jsonify
from flask import render_template
from flask_socketio import SocketIO,emit

import model

app = Flask(__name__)
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
    #看看你的
    return render_template('alogrithms.html')


@app.route('/getAlogrithms')
def show_user_profile():
    res = model.getAlogrithms()
    # show the user profile for that user
    return jsonify([user.to_json() for user in res])

@app.route('/getAlgStatus')
def getAlgStatus():
    return render_template('algstatus.html')

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

