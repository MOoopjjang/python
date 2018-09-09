#!python3
#-*- coding:utf-8 -*-

import re
import requests
import bs4
import os , sys
import random


WIKI_URL = 'https://en.wikipedia.org'
urlDict = {}


def splitUrl( _url , sposition ):
	rgx = re.compile('^(http|https):\/\/')
	mo = rgx.search( _url )
	filtUrl = _url.replace(mo.group() , '').split('/')[sposition]
	# print('filtUrl >> {}'.format(filtUrl))
	return filtUrl


def getProtocol( _url ):
	rgx = re.compile('^(((http|https):\/\/)|(www\.))')
	return rgx.search(_url).group()


def getExtLinks( _url , session ):
	global urlDict

	retLinks = []
	try:
		res = session.get(_url , timeout = 3)
		res.raise_for_status()
		bsObj = bs4.BeautifulSoup(res.text , 'html.parser')
		es = bsObj.findAll('a' , {'href':re.compile('^(http|https)((?!'+splitUrl(_url , 0)+').)*$')})
		
		for e in es:
			if e.attrs['href'] not in urlDict['ext']:
				urlDict['ext'].add(e.attrs['href'])
				retLinks.append(e.attrs['href'])
	except:
		print('error >> {}'.format(_url))

	return retLinks





def getIntLink( _url , session ):
	global urlDict

	print('getIntLink >> {}'.format(_url))
	strProtocol = getProtocol( _url )
	domain = splitUrl( _url , 0 )
	retLinks = []

	try:
		res = session.get(_url , timeout = 3)
		res.raise_for_status()
		bsObj = bs4.BeautifulSoup(res.text , 'html.parser' )
		es = bsObj.findAll('a' , {'href':re.compile('^(\.\.|\.|\/)')})
		hrefs = [strProtocol + domain + e.attrs['href'] for e in es]
		# print('hrefs >> {}'.format(hrefs))
		for e in hrefs:
			print('in >> {}'.format(e))
			if e not in urlDict['in']:
				urlDict['in'].add(e)
				retLinks.append(e)
	except:
		print('except >> {}'.format(_url))
	
	return retLinks


def loopLink( links , cbf ):
	for link in links:
		# i = random.randint(0 , len(links)-1)
		print(' go >> '+link)
		cbf(link)


def runExtLink( _url ):
	session = requests.session()
	eLinks = getExtLinks( _url , session )
	iLinks = getIntLink( _url , session )

	if len(eLinks) > 0:
		loopLink(eLinks , runExtLink )
	elif len(iLinks) > 0:
		loopLink(iLinks , runExtLink )
	else:
		sys.exit(0)



def runTrack( _url):
	runExtLink( WIKI_URL+'/wiki/'+ _url )



def main():
	global urlDict
	urlDict['in'] = set()
	urlDict['ext'] = set()

	input_search = input('input search text :: ')
	runTrack( input_search )




if __name__ == '__main__':
	main()

