#!python3
#-*- coding:utf-8 -*-


from abcdataaccess import ABCDataAccess
from defines.singleton import Singleton


@Singleton('FileDataAccessManager' , True)
class FileDataAccessManager( ABCDataAccess ):
	def __init__( self ):
		ABCDataAccess.__init__( self )


	def save(self ,  _data ):
		print('save')


	def findByAll( self ):
		print('findByAll')


	def findByEmail( self , email ):
		print('findByEmail')
