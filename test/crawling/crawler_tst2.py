#!python3
#-*- coding:utf-8 -*-


import requests
import bs4
import re


pages = set()


######################################  Wiki start ######################################## 
pageDict = {}
BASE_WIKI = 'https://en.wikipedia.org'


def splitUrl ( _url  , _index):
	tmp_url = _url
	tmp_rgx = re.compile('^(http|https):\/\/')
	m = tmp_rgx.search(_url)
	if m != None:tmp_url = _url.replace(m.group() , '')
	return tmp_url.split('/')[_index]

def getExtLink( _session , _url , _index ):
	res = _session.get(_url , timeout = 3)
	res.raise_for_status()
	bsObj = bs4.BeautifulSoup(res.text , 'html.parser' )
	# http나 https로 시작하고  wikipedia.org 문자열을 포함하지 않는다.
	extATags = bsObj.findAll('a' , {'href':re.compile('^http[a-z]*.((?!'+splitUrl( _url , _index )+').)*$')})

	retLinks = []
	for e in extATags:
		if e.attrs['href'] not in pageDict['ext']:
			pageDict['ext'].add(e.attrs['href'])
			retLinks.append(e)
	return retLinks

	

def getInLink( _session , _url ):
	res = _session.get('https://en.wikipedia.org'+_url , timeout = 3)
	res.raise_for_status()
	bsObj = bs4.BeautifulSoup(res.text , 'html.parser' )
	inTags = bsObj.findAll('a' , {'href':re.compile('^\/wiki\/')})

	retLinks = []
	for e in inTags:
		if e.attrs['href'] not in pageDict['in']:
			pageDict['in'].add(e.attrs['href'])
			retLinks.append(e)

	return retLinks




	
# def findLink( postUrl ):
# 	global pages

# 	url = 'https://en.wikipedia.org'+postUrl
# 	rgx = re.compile('^\/wiki\/')
# 	session = requests.session()
# 	res = session.get(url , timeout = 3)
# 	res.raise_for_status()
# 	bsObj = bs4.BeautifulSoup( res.text , 'html.parser' )

# 	title = bsObj.find('h1' , {'class':'firstHeading'}).get_text()
# 	content = bsObj.find('div' , {'id':'bodyContent'})
# 	print('title >> : {}'.format(title))
# 	print('toc >> : {}'.format(content.find('div' , {'id':'toc'})))

# 	for link in bsObj.find('div' , {'id':'bodyContent'}).findAll('a' , {'href':rgx}):
# 		href = link.attrs['href']
# 		if href not in pages:
# 			print('{}'.format(href))
# 			pages.add(href)
# 			findLink(href)


def wiki():
	global pageDict

	inputt = input(' 인물을 입력하세요 ::')
	url = BASE_WIKI + '/wiki/'+inputt
	pageDict['ext'] = set()
	pageDict['in'] = set()
	extLinks = getExtLink( requests.session() , url , 1 )
	inLinks = getInLink( requests.session() , '/wiki/'+inputt )

	if len(extLinks) > 0:
		for fl in extLinks:
			l = fl.attrs['href']
			print('{}'.format(l))
			extLinks = getExtLink( requests.session() , url , 0 )


	if len(inLinks) > 0:
		for fl in inLinks:
			l = fl.attrs['href']
			print('in >> {}'.format(l))


######################################  Wiki end ######################################## 	




def t2():
	session = requests.session()
	res = session.get('http://pythonscraping.com/pages/page3.html')
	res.raise_for_status()
	bsObj = bs4.BeautifulSoup(res.text , 'html.parser')
	for child in bsObj.find('table' , {'id':'giftList'}).children:
		print('{}'.format(child))


	print('-'*100)
	#sibiling
	# for sibiling in bsObj.find('table' , {'id':'giftList'}).tr.next_siblings:
	# 	print('{}'.format(sibiling))

	tr1 = bsObj.find('tr' , {'id':'gift1'})
	# print('{}'.format(tr1))


	# for index ,  td in  enumerate( bsObj.find('tr' , {'id':'gift1'}).children):
	# 	print('{} : {}'.format(index , td.get_text().strip()))
	# 	if index == 2:
	# 		ntd = td.next_sibling
	# 		print('{}'.format(ntd.find('img').get('src')))
			


	for img in bsObj.findAll('img' , {'src':re.compile('\.\.\/img\/gifts\/img[0-9]{1}.jpg')}):
		print('{}'.format(img.get('src')))






def t1():
	session = requests.session();
	res = session.get('https://nbamania.com/g2/bbs/board.php?bo_table=nbatalk&r=ok' , timeout = 3)
	res.raise_for_status()
	# print('body : {}'.format(res.text))
	bsObj = bs4.BeautifulSoup(res.text , 'html.parser')

	ems = bsObj.findAll('a' , {'class':'list_subject_a'})
	for index , e in enumerate( ems ):
		title = e.find('font' , {'class':'mobile_hide'})
		print('{}.{}'.format(index , title.get_text().strip()))





def main():
	# t1()
	# t2()

	wiki()

if __name__ == '__main__':
	main()