from sqlalchemy import create_engine
import pandas as pd
import pymysql
from flask import Flask, jsonify, request, redirect

conn = create_engine('mysql+pymysql://dodo:GCTAhTwrPPmJczcp@node1:3306/dodo?charset=utf8')


class Alogrithm:
    id = 0
    algorithm_name = ''
    algorithm_type = ''
    location = ''
    file_type=''
    description=''

    def __init__(self, id, algorithm_name, algorithm_type, file_type):
        self.id = id
        self.algorithm_name = algorithm_name
        self.algorithm_type = algorithm_type
        self.file_type = file_type

    def to_json(self):
        return {"id":self.id,
                "algorithm_name":self.algorithm_name,
                "algorithm_type":self.algorithm_type,
                "location":self.location,
                "file_type":self.file_type,
                "description":self.description}


def getAlogrithms():
    global conn
    df = pd.read_sql_query('select * from algorithms', conn)
    df = df.fillna(0)
    df = df.apply(pd.to_numeric, errors='ignore')
    n = df.shape[0]  # 行数
    data = []
    page = int(request.GET.get('page'))
    limit = int(request.GET.get('limit'))
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
    return jsonify(data)
