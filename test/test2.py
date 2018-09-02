#-*- coding: utf-8 -*-


import sys
# import pyperclip
import os
# import shelve
# import random
# import zipfile
import logging
import webbrowser
import requests
import bs4
import re

# import report

from urllib.request import urlopen



def init():
	logging.basicConfig(level = logging.DEBUG , format = ' %(asctime)s - %(levelname)s - %(message)s')
	


def func():
	html = urlopen('http://www.pythonscraping.com/pages/page3.html')
	bsObj = bs4.BeautifulSoup(html , 'html.parser')
	imgs = bsObj.findAll('img' , {'src':re.compile('\.\.\/img\/gifts\/img[0-9]\.jpg')})
	for img in imgs:
		print('{} : {}'.format(img['src'] , os.path.split(img['src'])[1]))
		s = img['src']
		dUrl = 'http://www.pythonscraping.com/'+ s[2:]

		dRes = requests.get(dUrl)
		dRes.raise_for_status()
		fw = open(os.getcwd()+'/'+os.path.split(img['src'])[1] , 'wb')
		for chunk in dRes.iter_content(100000):
			fw.write(chunk)
		fw.close()
		





def testNaverMovie():
	html = urlopen('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cnt&date=20180519')
	bsObj = bs4.BeautifulSoup(html , 'html.parser')
	table = bsObj.findAll('table' , {'class':'list_ranking'})

	tbody = table[0]
	trs = tbody.findAll('tr')

	for tr in trs:
		ranking = tr.find('td' , {'class':'ac'})
		title = tr.find('td' , {'class':'title'})

		if ranking != None and title != None:
			r = ranking.find('img').get('alt')
			t = title.find('a').get('title')
			print('ranking :{} -  title : {}'.format(r , t))


def main():
	init()

	func()

	# testNaverMovie()
			


if __name__ == '__main__':
	main()


