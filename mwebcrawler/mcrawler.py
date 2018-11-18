#!python3
#coding:utf-8


# Make by MOoop
# Desc
#	Image WebCrawler..


# History
# version 1.0
#	>>> create


import os , sys
import requests , bs4
import re
from mglobal import init , getLogger , getCurrentTime , getDefCurrentTime
import mzip
from multiprocessing import Process
import threading
import concurrent.futures



FREE_PROXY_URL = 'https://free-proxy-list.net/'
LOCAL_IP_URL = 'https://httpbin.org/ip'



class MCrawler:
	def __init__(self , lUrls = None , lSaveDirs = None , bMp = 0 , bZip = False , maxDepth = 0 , proxy = False):
		getLogger().info('__init__ called!!')
		self.__lUrls = lUrls
		self.__lSaveDirs = lSaveDirs
		self.__lProcs = []
		self.__bMp = bMp
		self.__bZip = bZip
		self.__maxDepth = maxDepth
		self.__nJobCount = 0
		self.__proxies = self.__select_proxy__( self.__get_proxies__())
		self.__isProxy = proxy


	def __del__(self):
		getLogger().info('__del__ called!!')
		del self.__lUrls[:]
		del self.__lSaveDirs[:]


	def __get_proxies__( self ):
		"""
		https://free-proxy-list.net/ 에서 ip:port 목록을 리스트로 반환한다.
		"""
		res = requests.get(FREE_PROXY_URL , timeout = 3)
		res.raise_for_status()

		proxy_list = []
		bsObj = bs4.BeautifulSoup(res.text , 'html.parser')
		tbody = bsObj.find('table' , {'id':'proxylisttable'}).find('tbody')
		for tr in tbody:
			tds = tr.findAll('td')
			proxy_list.append( ':'.join(map(lambda x:x.get_text() , tds[:2])))

		return proxy_list



	def __select_proxy__( self , proxy_list ):
		for info in proxy_list:
			try:
				pinfo = {}
				pinfo['http'] = 'http://'+info
				pinfo['https'] = 'http://'+info

				r = requests.get(LOCAL_IP_URL , proxies = pinfo , timeout = 3)
				print(r.json())
				return pinfo
			except Exception as ex:
				print('{}'.format(ex))





	def __chkValid__(self):
		if 	len(self.__lUrls) == 0 or len(self.__lSaveDirs) == 0:
			print('변수를 체크하세요.')
			sys.exit(0)

	def __getSaveFileName__(self , _downUrl):
		_,postName = os.path.split(_downUrl)
		now = getCurrentTime('%Y%m%d%H%M%S%f')
		# default 
		ext = '.jpg'
		rex = re.compile('\.(jpg|gif|png|bmp)$')
		mo = rex.search(postName)
		if mo != None:
			ext = postName[-4:]
			postName = postName[0:-4]	
	
		return postName+'_'+now+ext




	def __download_image__(self , _list , sSaveDir):
		getLogger().info('-- pid:{} --  image download start'.format(os.getpid()))
		session = requests.session()
		for downUrl in _list:
			try:
				if self.__isProxy:session.proxies = self.__proxies
				downUrlRes = session.get(downUrl)
				downUrlRes.raise_for_status()

				# 파일이름 생성
				nFileName = self.__getSaveFileName__(downUrl)
				wFileName = sSaveDir+'/'+nFileName
				getLogger().debug('save file path :'+wFileName)
				print('Downloading...%s'%(nFileName))
				fw = open(wFileName , 'wb')
				for chunk in downUrlRes.iter_content(100000):
					fw.write(chunk)
				fw.close()
			except:
				print('Download Error...%s'%(os.path.split(downUrl)[1]))
		getLogger().info('-- pid:{} --  image download end'.format(os.getpid()))
		



	def __nextDepth__(self , _depUrl , _soup , sSaveDir , _maxDepth ,  _depth):
		print('depth:'+str(_depth)+'#'*100)
		depthElms = _soup.select('a')
		getLogger().debug('depthElms count:{}'.format(len(depthElms)))
		if len(depthElms) > 0:
			hrefl = []
			for link in depthElms:
				if link.get('href') == None or len(link.get('href')) == 0 or link.get('href').startswith('http') == False:
					continue

				if _depUrl == link.get('href'):
					continue 	

				hrefl.append(link.get('href'))


			linkLen = len(hrefl)
			for index in range(0 , linkLen):
				print('-'*100)
				getLogger().info('Dep {}/{}'.format(_depth , _maxDepth))
				subDir = sSaveDir+'/Depth_'+str(_depth)+(os.path.split(hrefl[index])[1])
				if os.path.exists(subDir) == False or os.path.isdir(subDir) == False:
					os.mkdir(subDir)
				getLogger().info('{}/{} -- {}'.format(index , linkLen , hrefl[index]))
				getLogger().info('dir -- {}'.format(subDir))
				print('-'*100)
				
				self.__crawring__(hrefl[index] , subDir , _maxDepth , _depth)


	def __crawring__(self , sUrl , sSaveDir , _maxDepth ,  _depth):
		# getLogger().info('pid -- {}:{}'.format(os.getpid(),sUrl))
		getLogger().info('thread -- {}'.format(sUrl))
		try:
			session = requests.session()
			## Proxy 설정이 있다면..
			if self.__isProxy:
				print('#'*100)
				print('proxy ip :{}'.format(self.__proxies))
				print('#'*100)
				session.proxies = self.__proxies

			res = session.get(sUrl)
			res.raise_for_status()
			getLogger().info('text :{}'.format(res.text))
			soup = bs4.BeautifulSoup(res.text)
			imgElms = soup.select('img')
		
			getLogger().info('len :{}'.format(len(imgElms)))
			validUrl = []
			if len(imgElms) > 0:
				for elm in imgElms:
					downUrl = elm.get('src')

					#-- url 유효성 체크
					if downUrl == None:
						continue

					rgx = re.compile('^[.]{1,2}')
					mo = rgx.search(downUrl)
					if mo != None:
						rgx = re.compile('^https?.+(com|net|edu|org)')
						mo = rgx.search(sUrl)
						if mo != None:downUrl = str(mo.group())+'/'+downUrl[2:]
					elif downUrl.startswith('http') == False:downUrl = 'https:'+downUrl
						
					# 유효한 url을 리스트에 저장
					validUrl.append(downUrl)	

				#--File Download and Save
				getLogger().info('-url:{} , mp count : {}'.format(len(validUrl) , self.__bMp))
				nMPCount = self.__bMp
				if nMPCount > 1 and len(validUrl) > 5:
					# -- url count보다 Mp count가 클경우 url count값으로 mp count를 조절한
					if len(validUrl) < nMPCount:
						nMPCount = len(validUrl) -1

					threads = []
					bit = int(len(validUrl)/nMPCount)

					with concurrent.futures.ThreadPoolExecutor( max_workers = nMPCount ) as te:
						for index in range(0 , nMPCount):
							start = index * bit
							end = start + bit
							if index == (nMPCount - 1):
								end = len( validUrl )
							th = te.submit(self.__download_image__ , validUrl[start:end] , sSaveDir)
							threads.append( th )

						for th in concurrent.futures.as_completed( threads ):
							print('{}'.format(th.result()))

				else:
					self.__download_image__(validUrl , sSaveDir)
					

				# Zip압축
				if self.__bZip == True:
					mzip.MZip.compress(sSaveDir , logging)

			# NEXT DEPTH	
			getLogger().info('_maxDepth :{} , _depth:{}'.format(_maxDepth , _depth))
			if _maxDepth != 0 and _depth < _maxDepth:
				_depth+=1
				self.__nextDepth__(sUrl , soup, sSaveDir , _maxDepth , _depth )
		except Exception as ex:
			getLogger().info('{}'.format(ex))

		return '{} ==> complete'.format(sUrl)


	def run( self ):
		self.__chkValid__()

		# -- Process Count
		self.__nJobCount = len(self.__lUrls)

		if self.__bMp > 1 and self.__nJobCount > 1:
			with concurrent.futures.ProcessPoolExecutor( max_workers = self.__nJobCount ) as pe:
				tResultList = []
				for i in range(self.__nJobCount):
					tResultList.append(pe.submit( self.__crawring__,self.__lUrls[i] , self.__lSaveDirs[i] , self.__maxDepth , 1 ))

				for th in concurrent.futures.as_completed(tResultList):
					print('{}'.format(th.result()))
		else:
			for i in range( 0  , self.__nJobCount ):
				self.__crawring__(self.__lUrls[i] , self.__lSaveDirs[i] , self.__maxDepth , 1)



	def getCrawlerResult(self):
		pass		


