from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/kifrs1001', methods=['GET'])
def listingkifrs1001():
    result = list(db.kifrs1001.find({}, {'_id':0}).sort('no'))  
    return jsonify({'result':'success', 'msg':'GET 연결되었습니다!', 'standards':result})

@app.route('/kifrs1002', methods=['GET'])
def listingkifrs1002():
    result = list(db.kifrs1002.find({}, {'_id':0}).sort('no'))  
    return jsonify({'result':'success', 'msg':'GET 연결되었습니다!', 'standards':result})

@app.route('/kifrs1007', methods=['GET'])
def listingkifrs1007():
    result = list(db.kifrs1007.find({}, {'_id':0}).sort('no'))  
    return jsonify({'result':'success', 'msg':'GET 연결되었습니다!', 'standards':result})




if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)

