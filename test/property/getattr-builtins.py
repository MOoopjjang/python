#!python
#-*- coding:utf-8 -*-



class GetAttr:
	eggs = 88
	def __init__( self ):
		self.spam = 77

	def __len__( self ):
		print('__len__:42')
		return 42

	def __getattr__( self , attr ):
		print('__getattr__ : '+attr)
		if attr == '__str__':
			return lambda *args:'[Getattr str]'
		else:
			return lambda *args:None


class GetAttribute(object):
	eggs = 88
	def __init__( self ):
		self.spam = 77

	def __len__( self ):
		print('__len__ : 42')
		return 42

	def __getattribute__( self , attr ):
		print('__getattribute__ : '+attr)
		if attr == '__str__':
			return lambda *args:'[GetAttribute str]'
		else:
			return lambda *args:None