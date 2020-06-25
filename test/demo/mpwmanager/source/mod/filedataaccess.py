#!python3
#-*- coding:utf-8 -*-

'''
Data를  file로 저장/수정/삭제/read하는 기능을 제공
'''

from source.mod.abcdataaccess import ABCDataAccess
import shelve


class FileDataAccessManager( ABCDataAccess ):
	def __init__( self ):
		ABCDataAccess.__init__( self )
		self._path = None


	def load(self , _path):
		self._path = _path
		return self


	def save(self , _key , _data ):
		if _key in shelve.open(self._path):
			return True
		with shelve.open(self._path) as sh:
			sh[_key] = _data
		return True

			
	def remove( self , _key ):
		with shelve.open( self._path ) as sh:
			del sh[_key]


	def findByAll( self ):
		with shelve.open(self._path) as sh:
			cache = dict(sh) if len( sh ) > 0 else {}
		return cache


	def findByOne( self , _key ):
		if len(shelve.open(self._path)) == 0:
			return None

		with shelve.open(self._path) as sh:
			return sh.get(_key , None)



