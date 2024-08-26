#!python3
#-*- coding:utf-8 -*-

# Make by:
#	MOoop
#
# History
# 	v1.0 2018.04.22     
#		>>>  Create
# Desc:
#   지정된 디렉토리부터 원하는 파일을 검색하여 출력및 파일로 저장한다

import mglobal
import os , sys
import re
import array
from unicodedata import normalize



class Search:

	def __init__(self , output = None):

		self.__searchList = []
		# self.__searchList = array.array('u',)
		self.orgpath = os.path.abspath('.')
		self.__srcdir = None
		self.__fns = None
		self.__bOutput = output
		self.__totCount = 0
		self.__maxFileInfo = {}

	def __del__(self):
		del self.__searchList[:]
		self.__maxFileInfo.clear()


	def __iter__( self ):
		print('-'*100)
		print('result:')
		for item in self.__searchList:
			yield item

		print('-'*100)


	def __saveInfo__(self , path):
		# 가장큰 파일 정보 셋팅
		if os.path.isfile(path):
			saveSize = self.__maxFileInfo.get('size' , 0)
			curSize = os.path.getsize(path)
			_,fname = os.path.split(path)
			if curSize > saveSize:
				self.__maxFileInfo['path'] = fname
				self.__maxFileInfo['size'] = curSize

        # 검색 파일 count
		self.__totCount +=1

		# 출력할 리스트 셋팅
		self.__searchList.append(path)




	## 결과를 file로 저장.
	def __saveFile(self):
		if self.__bOutput != None and len(self.__searchList)>0:
			mglobal.getLogger().debug('[__saveFile]curDir::'+os.getcwd())
			curDir = os.getcwd()
			sf = curDir+'/'+self.__bOutput

			if os.path.exists(sf) == True:os.unlink(sf)
			print('save file::'+sf)
			with open(sf , 'a') as fw:
				for fn in self.__searchList:
					fw.write(fn.strip()+'\n')
				fw.flush()


	def setSearchInfo(self , srcdir , filename):
		# 검색디렉토리 위치 셋팅
		if srcdir == '.':
			self.__srcdir = os.getcwd()
		elif srcdir == '../':	
			self.__srcdir,_ = os.path.split(os.getcwd())
		else:
			self.__srcdir = srcdir	


		# 검색할 파일이름 셋팅
		fn = None
		if filename == None:
			fn = '*'
		else:
			mglobal.getLogger().debug('filename :{}'.format(filename))
			if len(filename) == 1 and filename == '*':
				fn = '*'
			elif '*' in filename:
				convStr = filename.replace('*','(.*)')
				# convStr += '(.+)'
				fn = convStr
			else:	
				fn = filename		

		mglobal.getLogger().debug('fn :{}'.format(fn))	
		self.__fns = fn.split('|')




	def find(self):
		if self.__srcdir == None or self.__fns == None:
			print('Usage : mfinder.py [dir path] [search file name]')
			sys.exit(0)


		if os.path.exists(self.__srcdir) == True and os.path.isdir(self.__srcdir) == True:
			os.chdir(self.__srcdir)
			for d , s , filenames in os.walk(self.__srcdir):
				for fn in filenames:
					if '*' in self.__fns:
						print(d+'/'+fn.strip())
					elif len(self.__fns) == 1:
						regex = re.compile(self.__fns[0])
						norstr = normalize('NFC' , fn.strip())
						mo = regex.search(norstr)
						if mo != None:self.__saveInfo__(os.path.join(d , norstr))
							# mglobal.getLogger().debug('{} : {} : {}'.format(fn , type(fn) , len(fn)))
							
					else:
						for e in self.__fns:
							regex = re.compile(e)
							norstr = normalize('NFC' , fn.strip())
							if regex.search(norstr) !=None:self.__saveInfo__(os.path.join(d , norstr))
								
			
		else:
			raise Exception('{} not found!!!'.format(self.__srcdir))	

		# 작업디렉토리를 현재 위치로 변겨야	
		os.chdir(self.orgpath)	
		self.__saveFile()


	def getResultList(self):
		return self.__searchList

	def print(self):
		if len(self.__searchList) > 0:
			for l in self.__searchList:
				print('%s'%(l.strip()))


		print('='*100)		
		print('\t\ttotalCount ::'+str(self.__totCount))
		print('\t\tmax :{}::{}'.format(self.__maxFileInfo.get('path','unknown') , self.__maxFileInfo.get('size' , 0)))
		print('='*100)





		