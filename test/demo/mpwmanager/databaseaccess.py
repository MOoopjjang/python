#!python3
#-*- coding:utf-8 -*-

from abcdataaccess import ABCDataAccess
from defines.singleton import Singleton

@Singleton('DatabaseAccessManager' , True)
class DatabaseAccessManager( ABCDataAccess ):

	def load(self , _path):
		print('load')
		return self

	def save(self ,  _data ):
		print('save')

	def remove( self , _key ):pass
		


	def findByAll( self ):
		print('findByAll')


	def findByOne( self , email ):
		print('findByEmail')