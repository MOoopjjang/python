#!python3
#-*- coding:utf-8 -*-


from abcdataaccess import ABCDataAccess
from defines.singleton import Singleton
import shelve


@Singleton('FileDataAccessManager' , True)
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
			
		


	def findByAll( self ):pass



	def findByEmail( self , _key ):
		if len(shelve.open(self._path)) == 0:
			return False

		with shelve.open(self._path) as sh:
			return sh[_key]
