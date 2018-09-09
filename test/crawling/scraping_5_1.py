#!python3
#-*- coding:utf-8 -*-


import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup



downDirectory = 'download'
baseUrl = 'http://pythonscraping.com'


def getAbsoluteURL( baseUrl , source ):
	if source.startswith('http://www.'):
		url = 'http://'+source[11:]
	elif source.startswith('http://'):
		url = source
	elif source.statswith('www.'):
		url = source[4:]
		url = 'http://'+source
	else:
		url = baseUrl + '/' + source

	if baseUrl not in url:
		return None
	return url


def getDownloadPath( baseUrl , absoluteUrl , downloadDirectory ):
	path = absoluteUrl.replace('www.' , '')
	path = path.replace(baseUrl , '')
	path = downloadDirectory + path
	directory = os.path.dirname( path )

	if not os.path.exists(directory):
		os.makedirs(directory)

	return path



def main():
	html = urlopen('http://www.pythonscraping.com')
	bsObj = BeautifulSoup(html , 'html.parser')
	downList = bsObj.findAll(src = True )

	for dl in downList:
		fileUrl = getAbsoluteURL( baseUrl , dl['src'] )
		if fileUrl != None:
			print('{}'.format(fileUrl))

		urlretrieve(fileUrl , getDownloadPath(baseUrl , fileUrl , downDirectory) )	



if __name__ == '__main__':
	main()




