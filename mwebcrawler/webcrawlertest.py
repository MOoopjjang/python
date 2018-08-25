#!python
#-*- coding:utf-8 -*-


# Desc:
#	webcrawler Test Module



import requests
import bs4
import sys , os
import re
from mglobal import init , getLogger ,setLoggingLevel , getCurrentTime , getDefCurrentTime


d = {}


def saveFileName(_imgUrl):
	fName = os.path.split(_imgUrl)[1]
	getLogger().debug('file name ::{}'.format(fName))

	ext = '.jpg'
	reg = re.compile(r'[.](jpg|png|bmp|gif)$')
	mo = reg.search(fName)
	if mo == None:
		return fName+ext
	return fName



def loadProperties():
	global d

	fread = open(sys.argv[1] , 'r')
	dir_list = []
	url_list = []
	for line in fread:
		if line.startswith('wc.dir') == True:
			sd = line.split(':::')[1]
			if sd[-1] == '\n':
				sd = sd[0:-1]
			dir_list.append(sd)
		elif line.startswith('wc.url') == True:
			url = line.split(':::')[1]
			if url[-1] == '\n':
				url = url[0:-1]
			url_list.append(url)

	d['dirs'] = dir_list
	d['urls'] = url_list


def run():
	global d

	getLogger().debug('adfadfa')
	url = d['urls'][0]
	getLogger().debug('-- url:{}'.format(url))
	res = requests.get(url , timeout = 3)
	getLogger().debug(res.text)
	res.raise_for_status()
	soup = bs4.BeautifulSoup(res.text)
	elms = soup.select('img')
	getLogger().debug('-- step1 len:{}'.format(len(elms)))

	downUrls = []
	for e in elms:
		imgUrl = e.get('src')
		# getLogger().debug('-- step2 imgUrl:{}'.format(imgUrl))
		if imgUrl.startswith('http') == False:
			continue
		downUrls.append(imgUrl)

	getLogger().debug('-- downUrls len:{}'.format(len(downUrls)))
	for durl in downUrls:
		fw = None
		try:
			getLogger().debug('-- step2 durl:{}'.format(durl))
			downRes = requests.get(durl , timeout = 3)
			downRes.raise_for_status()

			fName = saveFileName(durl)
			getLogger().debug('-- fName :{}'.format(fName))

			fw = open(d['dirs'][0]+'/'+fName , 'wb')
			print('Downloading.. {}'.format(fName))
			for chunk in downRes.iter_content(100000):
				fw.write(chunk)
		except:
			print('Downloading Failed.. {}'.format(fName))
		finally:
			if fw != None:
				fw.close()


def main():
	init()

	setLoggingLevel('info')

	loadProperties()

	run()



if __name__ == '__main__':
	main()