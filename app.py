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

@app.route('/kifrs')
def kifrs():
   return render_template('kifrs.html')

@app.route('/kgaap')
def kgaap():
   return render_template('kgaap.html')

@app.route('/kifrs/<num>')
def link_kifrs_page(num):
   return render_template('detail.html')

@app.route('/kgaap/<num>')
def link_kgaap_page(num):
   return render_template('detail.html')

# index 및 content API
# 동적 collection : db[변수]
@app.route('/detail/<num>')
def getstdnum(num):
    if int(num) > 1000:
        kifrs = list(db["kifrs"+num].find({}, {'_id':0}).sort('no'))
        return jsonify({'result':'success', 'gaap':kifrs})
    else:
        kgaap = list(db["kgaap"+num].find({}, {'_id':0}).sort('no'))
        return jsonify({'result':'success', 'gaap':kgaap})

# 리스트 API
@app.route('/standard/<type>')
def getstdlist(type):
    stdlist= list(db[type+"list"].find({}, {'_id':0}).sort('no'))
    return jsonify({'result':'success', 'stdlist':stdlist})
    
# @app.route('/search/<num>')
# def find_word(num):
  #  getstd = list(db["kifrs"+num].find({}, {'_id':0}).sort('no'))
#    search_value = request.form['search_value']
 #   print(search_value)
  #  search_list = []   
  #  for i in getstd:
    #   if search_value in i["content"]:
      #    i0 = i['i0']
        #  i1 = i['i1']
 #         i2 = i['i2']
   #       i3 = i['i3']
     #     search_list.append(i0)
       #   search_list.append(i1)
         # search_list.append(i2)
#          search_list.append(i3)
  #        search_list = list(set(search_list))
    #      search_list.remove('')
   # return jsonify({'result':'success', 'search_list':search_list})


    

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)

