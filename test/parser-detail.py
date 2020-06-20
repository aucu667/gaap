import requests
from bs4 import BeautifulSoup

url = 'http://www.kasb.or.kr/fe/bbs/NR_view.do?bbsCd=1017&bbsSeq=34325&extSearchKey=1017&currentPage=1&rowPerPage=10&ctgCd=&strDd=&endDd=&searchKey=1000&searchVal='
result = requests.get(url)
soup = BeautifulSoup(result.text, 'html.parser')
tables = soup.find("tbody")
trs = tables.find_all("tr")

# 테이블 파싱
for tr in trs:
    th = tr.find("th").text
    td = tr.find("td").text.strip()  
    print(th, td)
    # if tr.find('a')['href'] != None: TypeError: 'NoneType' object is not subscriptable    a태그에서 href를 가져와서 자동다운로드하려고함
        # donwload_url = tr.find('a')['href']
        # print(th, td, donwload_url)

# 컨텐츠 파싱은 진행중
# contents_desc = soup.find_all("#contents-desc") 안나옴......



