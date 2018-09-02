#!python3
#-*- coding:utf-8 -*-

from bs4 import BeautifulSoup
from urllib.request import urlopen
import logging
import webbrowser
import re
import random

def init():
	logging.basicConfig(level = logging.DEBUG , format = '%(asctime)s-%(levelname)s-%(message)s')

def naverMovie():
	getHtml = urlopen('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cnt&date=20180519')
	bsObj = BeautifulSoup(getHtml , 'html.parser')
	table = bsObj.find('table' , {'class':'list_ranking'})
	logging.debug('--{}--'.format(table))
	tbody = table.find('tbody')
	logging.debug('tbody : {}'.format(tbody))
	trs = tbody.findAll('tr')
	for tr in trs:
		rankingtd = tr.find('td' , {'class':'ac'})
		titletd = tr.find('td' , {'class':'title'})
		if rankingtd != None and titletd != None:
			r = rankingtd.find('img').get('alt')
			t = titletd.find('a').get('title')
			print('{}:{}'.format(r,t))




##  Wiki Scraping  start ##

pages = set()
def getLink(_url):
	html = urlopen('https://en.wikipedia.org'+_url)
	bsObj = BeautifulSoup(html , 'html.parser')
	# return bsObj.find('div' , {'id':'bodyContent'}).findAll('a' , href = re.compile('^(/wiki/)((?!:).)*$'))
	return bsObj.find('div' , {'id':'bodyContent'}).findAll('a' , href = re.compile('^(/wiki/)'))


def wiki():
	global pages
	links = getLink('/wiki/Kevin_Mitnick')
	for link in links:
		if link.get('href') != None and link.get('href') not in pages:
			pages.add(link.get('href'))
			logging.debug('- {} -'.format(link.get('href')))
			getLink(link.get('href'))
	# while len(links) > 0:
	# 	link = links[random.randint(0 , len(links))].get('href')
	# 	print('{}'.format(link))
	# 	getLink(link)


	for page in pages:
		print('page : {}'.format(page))


## Wiki Scraping End ##	


infoList = []
def getContent(_posturl):
	# logging.debug('openurl : {}'.format('https://en.wikipedia.org'+_posturl))
	html = urlopen('https://en.wikipedia.org'+_posturl)
	bsObj = BeautifulSoup(html , 'html.parser')
	return bsObj.find('div' , {'id':'content'})

# def getBodyContent(_bsObj):


def splitInfo(_url):
	global infoList
	info = {}
	# logging.debug('- t : {}'.format(type(content)))
	content = getContent(_url)
	title = content.find('h1' , {'id':'firstHeading'})
	# title
	info['title'] = title.get_text()

	
	bodyContent = content.find('div' , {'id':'bodyContent'})
	firstLink = None
	for h2 in bodyContent.findAll('h2'):
		if h2.find('span' , {'class':'mw-editsection'}) != None:
			if h2.find('span' , {'class':'mw-editsection'}).find('a') != None \
			and h2.find('span' , {'class':'mw-editsection'}).find('a').get_text() == 'edit':
				firstLink = h2.find('span' , {'class':'mw-editsection'}).find('a')
				break

	if firstLink != None and firstLink.get('href') != None:info['url']=firstLink.get('href')

	logging.info('title : {} , l : {}'.format(title.get_text() , info['url']))
	infoList.append(info)
	return bodyContent


def wikiScrapingTitle(_posturl):
	bodyContent = splitInfo(_posturl)
	links = bodyContent.findAll('a' , href = re.compile('^(/wiki/)((?!:).)*$'))
	for link in links:
		if link.get('href') != None:
			if link.get('href') not in pages:
				pages.add(link.get('href'))
				wikiScrapingTitle(link.get('href'))

		

def main():
	init()
	# naverMovie()

	# wiki()

	wikiScrapingTitle('/wiki/Kevin_Mitnick')

	logging.debug('{}'.format(infoList))

if __name__ == '__main__':
	main()


