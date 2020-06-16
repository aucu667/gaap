import os
from time import sleep

# hwp 가지고 있는 책 목록들
path = 'c:/Users/Admin/Documents/From40/Sparta/gaap/parsing/pyhwp.py'

# hwp5txt 파일
exefile = 'hwp5txt' 

def hwp2txt (path): #절대경로 포함 파일명
    res = []
    for root, dirs, files in os.walk(path):
        rootpath = os.path.join(os.path.abspath(path), root)
        for file in files:
            filepath = os.path.join(rootpath, file)
            res.append(filepath)
        for result in res:
            result = '"'+result+'"'
            os.system(exefile+' '+result)
            sleep(1)

if __name__=="__main___":
    hwp2txt(path)