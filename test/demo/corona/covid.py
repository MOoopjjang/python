#!python3
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
from urllib.request import urlopen

COVID_URL = 'http://ncov.mohw.go.kr/'


if __name__ == '__main__':
    try:
        html = urlopen(COVID_URL)
        bObj = BeautifulSoup(html , 'html.parser')
        divs = bObj.findAll('div' , {'class':'liveNum_today_new'})
        lis = divs[0].findAll('li')
        totalTodayCovidCount = sum(int(liE.find('span' , {'class','data'}).text) for liE in divs[0].findAll('li'))
        print(f'>>>>> 오늘 국내발생자 {totalTodayCovidCount} <<<<<<<<')
    except:
        print('error')


