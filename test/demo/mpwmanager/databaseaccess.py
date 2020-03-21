#!python3
#-*- coding:utf-8 -*-

from abcdataaccess import ABCDataAccess
from defines.singleton import Singleton

@Singleton('DatabaseAccessManager' , True)
class DatabaseAccessManager( ABCDataAccess ):

	def save(self ,  _data ):
		print('save')


	def findByAll( self ):
		print('findByAll')


	def findByEmail( self , email ):
		print('findByEmail')