#!python3
#-*- coding:utf-8 -*-


import asyncio
import re
import requests
import webbrowser
import sys , os
from bs4 import BeautifulSoup
import urllib.request
from urllib.request import Request, urlopen
from urllib.request import URLError, HTTPError
from urllib.parse import quote

import requests




"""
 기능 :
   - crawling 기능
   - url parsing기능
   - 검색어 연동기능..
"""


async def crawling(_urls , _dir):
	print('len : %d'%len(_urls))
	if len(_urls) > 0:
		os.mkdir(_dir)
		session = requests.session()
		for index , url in enumerate(_urls):
			try:
				res = session.get(url)
				res.raise_for_status()
				
				s = url.split('/')
				filename = str(index)+'_'+s[-1]

				rgx = re.compile('\.(jpg|png|gif|JPG|GIF|PNG)')
				mo = rgx.search(filename)
				if mo == None:filename+='.jpg'
				fullPath = _dir+'/'+filename
				print('Downloading ... {}'.format(fullPath))
				with open(fullPath , 'wb') as fw:
					for chunk in res.iter_content(100000):
						fw.write(chunk)
			except KeyboardInterrupt:
				break
			except:pass


async def parsing(_text):
	bsObj = BeautifulSoup(_text , 'html.parser')
	mainE = bsObj.findAll('div' , {'class':'rg_meta notranslate'})
	print(len(mainE))
	imgUrls = []
	for e in mainE:
		try:
			stre = str(e)
			start = len('<div class="rg_meta notranslate">')
			end = len(stre) - len('</div>')
			loads = stre[start:end]
			start = loads.find('ou\":')
			ss = loads[start+5:]
			end = ss.find(',')-1
			imgUrls.append(ss[:end])
		except:pass
	return imgUrls


async def search(keyword):
	url = 'https://www.google.com/search?q=' + quote(
                ' '.join(keyword)) + '&espv=2&biw=1366&bih=667&site=webhp&source=lnms&tbm=isch' + '&tbs=' + '&sa=X&ei=XosDVaCXD8TasATItgE&ved=0CAcQ_AUoAg'
	
	"""
	urllib version
	"""
	# headers = {}
	# headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
	# req = urllib.request.Request(url, headers=headers)
	# resp = urllib.request.urlopen(req)
	# respData = str(resp.read())
	# return respData

	"""
	requests version
	"""
	header = {}
	header['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
	res = requests.get(url , headers = header )
	return res.text


async def main():	
	keyword = sys.argv[1:]
	html = await search(keyword)
	imgUrls = await parsing(html)
	await crawling(imgUrls , os.getcwd()+'/'+('_'.join(keyword)))


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()


