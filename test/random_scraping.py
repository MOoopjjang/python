#!python3
#-*- coding:utf-8 -*-

import os , sys
from urllib.request import urlopen
import re
from bs4 import BeautifulSoup
import logging
import random


extUrls = set()
intUrls = set()

count = 0;

def init():
	logging.basicConfig(level = logging.DEBUG , format = ' %(asctime)s - %(levelname)s - %(message)s')



def getExternalLink(_bsObj , _curl):
	extList = []
	logging.debug('curl:{}'.format(_curl))
	links = _bsObj.findAll('a' , href = re.compile('^(http|www)((?!'+_curl+').)*$'))
	logging.debug('c : {}'.format(len(links)))
	for link in links:
		extList.append(link.get('href'))
		print('{}'.format(link.get('href')))

	return extList


def getInternalLink(_bsObj):
	pass	


def splitUrl(_url):
	rgx = re.compile(r'^(http|www).+(com|net|edu|org)')
	mo = rgx.search(_url)
	sUrl = None
	if mo != None:sUrl = mo.group().split('//')[-1]
	return sUrl

def entry(_url):
	global count
	if count == 10:
		print('scriping exit')
		sys.exit(0)

	html = urlopen(_url)
	bsObj = BeautifulSoup(html , 'html.parser')
	# links = bsObj.findAll('a')
	# logging.debug('c : {}'.format(len(links)))

	count +=1
	cUrl = splitUrl(_url)
	extlinks = getExternalLink(bsObj , cUrl)
	logging.debug('extlink count : {}'.format(len(extlinks)))
	# intlinks = getInternalLink(bsObj)
	if len(extlinks) > 0:
		logging.debug('count:{} -----------------'.format(count))
		rlink = extlinks[random.randint(0 , len(extlinks)-1)]
		# while splitUrl(rlink)
		logging.debug('search ... {}'.format(rlink))
		entry(rlink)
	else:
		pass

	


def main():
	init()
	entry('http://oreilly.com')
	


if __name__ == '__main__':
	main()


