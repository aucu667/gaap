from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

aaa= list(db.kgaap1.find({}, {'_id':0}))

search_list = []
for aa in aaa:
    if '목적' in aa["content"]:
        i0 = aa['i0']
        i1 = aa['i1']
        i2 = aa['i2']
        i3 = aa['i3']
        search_list.append(i0)
        search_list.append(i1)
        search_list.append(i2)
        search_list.append(i3)
        search_list = list(set(search_list))
        search_list.remove('')
print(search_list)



kkk = "한국채택"
if "한국" in kkk:
    print("k")

