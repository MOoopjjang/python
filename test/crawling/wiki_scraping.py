#!python3
#-*- coding:utf-8 -*-


# Make by MOoop
# Desc
#	wiki page에서 제목과 첫번째 edit link를 수집하는 scraper



import bs4
from urllib.request import urlopen
import re
import logging


infoList = []
pages = set()

def scraping(_purl):
	global infoList
	global pages

	info = {}
	html = urlopen('https://en.wikipedia.org'+_purl)
	bsObj = bs4.BeautifulSoup(html , 'html.parser')
	try:
		print('edit url : {}'.format(bsObj.find('li' , {'id':'ca-edit'}).find('span').find('a').get('href')))
		print('url : {}'.format('https://en.wikipedia.org'+_purl))
		print('title :{}'.format(bsObj.find('h1' , {'id':'firstHeading'}).get_text()))
		print('-'*100)
	except:
		pass
	
	for link in bsObj.findAll('a' , href = re.compile('^(/wiki/)')):
		if link.get('href') != None and link.get('href') not in pages:
			pages.add(link.get('href'))
			scraping(link.get('href'))


def main():
	scraping('/wiki/Kevin_Mitnick')



if __name__ == '__main__':
	main()