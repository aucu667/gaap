#-*- coding: utf-8 -*-

import requests 
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}



with open("1001.html", encoding='utf-8') as fp:
    soup = BeautifulSoup(fp, 'html.parser')

    contents = soup.select('body > div:nth-child(19) > div:nth-child(3)')

    for content in contents:
        # movie 안에 a 가 있으면,
            print (content.text)