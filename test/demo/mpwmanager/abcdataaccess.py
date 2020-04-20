#!python3
#-*- coding:utf-8 -*-

from abc import ABCMeta , abstractmethod

class ABCDataAccess( metaclass = ABCMeta ):

	@abstractmethod
	def load(self , _path):pass

	@abstractmethod
	def save(self ,  _data ):pass

	@abstractmethod
	def remove( self , _key ):pass

	@abstractmethod
	def findByAll( self ):pass

	@abstractmethod
	def findByOne( self , email ):pass