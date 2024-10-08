#!python3
#-*- coding:utf-8 -*-


'''
Data를 db | file로 저장/수정/삭제/read하는 기능을 제공
'''

from src.python.mod.filedataaccess import FileDataAccessManager
from src.python.mod.databaseaccess import DatabaseAccessManager


class MDataAccessManager:
	def __init__( self , _tag = 'FILE_SAVE'):
		self._repositoryDict = {
			'FILE_SAVE':FileDataAccessManager(),
			'DB_SAVE':DatabaseAccessManager()
		}
		self._tag = _tag
		self._repository = self._repositoryDict[self._tag]

	def load(self , _path ):
		return self._repository.load(_path)

	def save( self , _key , _data):
		self._repository.save( _key , _data )
		return self

	def remove( self , _key ):
		self._repository.remove(_key)
		return self


	def findByAll( self ):
		return self._repository.findByAll()


	def findByOne( self , _key ):
		return self._repository.findByOne( _key )

