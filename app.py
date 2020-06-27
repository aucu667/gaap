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

@app.route('/admin')
def admin():
   return render_template('admin.html')

@app.route('/kifrsfaq')
def kifrsfaq():
   return render_template('kifrsfaq.html')

@app.route('/kgaapfaq')
def kgaapfaq():
   return render_template('kgaapfaq.html')

@app.route('/popup', methods=['GET'])
def popup():
   return render_template('popup.html')

# index 및 content API
# 동적 collection : db[변수]
@app.route('/detail/<num>', methods=['GET'])
def getstdnum(num):
    if int(num) > 1000:
        kifrs = list(db["kifrs"+num].find({}, {'_id':0}).sort('no'))
        return jsonify({'result':'success', 'gaap':kifrs})
    else:
        kgaap = list(db["kgaap"+num].find({}, {'_id':0}).sort('no'))
        return jsonify({'result':'success', 'gaap':kgaap})

# 리스트 API
@app.route('/standard/<type>', methods=['GET'])
def getstdlist(type):
    stdlist= list(db[type+"list"].find({}, {'_id':0}).sort('no'))
    return jsonify({'result':'success', 'stdlist':stdlist}) 

@app.route('/search', methods=['POST'])
def find_word():
   search_value = request.form['search_value']
   search_db = request.form['search_db']
   
   getstds = list(db["kifrs"+search_db].find({}, {'_id':0}).sort('no'))   

   search_result = [] 
   for i in getstds:
      if not isinstance(i["content"], str): # 스트링이 아닐경우는 하지말고 
         continue # for에서 조건이 맞으면 continue 아래는 실행하지 않음
      if search_value in i["content"]: # TypeError: argument of type 'float' is not iterable
            search_result.append(i["i0"])
            search_result.append(i["i1"])
            search_result.append(i["i2"])
            search_result.append(i["i3"])
            search_result = list(set(search_result))
   return jsonify({'result':'success', 'final_result': search_result})

@app.route('/searchstd', methods=['POST'])
def find_word_std():
   search_value = request.form['search_value']
   search_db = request.form['search_db']
   kifrs_number_list = ['1001', '1002', '1007', '1008', '1010', '1012', '1016', '1019', '1020', '1021', '1023', '1024', '1026', '1027', '1028', '1029', '1032', '1033', '1034', '1036', '1037', '1038', '1039', '1039', '1040', '1041', '1101', '1102', '1103', '1104', '1105', '1106', '1107', '1108', '1109', '1110', '1111', '1112', '1113', '1114', '1115', '1116', '2101', '2102', '2105', '2106', '2107', '2110', '2112', '2114', '2116', '2117', '2119', '2120', '2121', '2122', '2123', '2010', '2025', '2029', '2032']
   kgaap_number_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33']
   search_result = [] 

   if search_db=="kifrs":
      for i in kifrs_number_list:
         getstds = list(db["kifrs"+i].find({}, {'_id':0}).sort('no'))
         for j in getstds:
               if not isinstance(j["content"], str): # 스트링이 아닐경우는 하지말고 
                  continue # for에서 조건이 맞으면 continue 아래는 실행하지 않음
               if search_value in j["content"]: # TypeError: argument of type 'float' is not iterable
                  search_result.append(i)
   else:
      for i in kgaap_number_list:
         getstds = list(db["kgaap"+i].find({}, {'_id':0}).sort('no'))
         for j in getstds:
               if not isinstance(j["content"], str): # 스트링이 아닐경우는 하지말고 
                  continue # for에서 조건이 맞으면 continue 아래는 실행하지 않음
               if search_value in j["content"]: # TypeError: argument of type 'float' is not iterable
                  search_result.append(i)
      
   search_result = list(set(search_result))
   return jsonify({'result':'success', 'final_result': search_result})   
    

@app.route('/reviews', methods=['POST'])
def write_review():
    title_receive = request.form['title_give']
    category_receive = request.form['category_give']
    review_receive = request.form['review_give']

    review = {
       'title': title_receive,
       'category': category_receive,
       'review': review_receive
    }

    db.reviews.insert_one(review)
    return jsonify({'result': 'success', 'msg': 'FAQ가 성공적으로 작성되었습니다.'})


@app.route('/reviews', methods=['GET'])
def read_reviews():
    reviews = list(db.reviews.find({},{'_id':0}))
    return jsonify({'result': 'success', 'reviews': reviews})




if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)

