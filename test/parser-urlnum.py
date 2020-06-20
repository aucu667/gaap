import requests
from bs4 import BeautifulSoup

# for i in range(135): 아래 currenpage에 숫자 {i}넣어야 함
url = f'http://www.kasb.or.kr/fe/bbs/NR_list.do?bbsCd=1017&bbsSeq=&extSearchKey=1017&currentPage=1&rowPerPage=10&ctgCd=&strDd=&endDd=&searchKey=1000&searchVal='
result = requests.get(url)
soup = BeautifulSoup(result.text, 'html.parser')
divs = soup.find_all("div", {"class":"download-wrap"})[3:]
url_num_list = []
for div in divs:
    a = div.find("a")
    onclick = a["onclick"]
    onclick_num = int(onclick.split('(')[1].split(')')[0][1:-1])
    url_num_list.append(onclick_num)
print(url_num_list)

            




