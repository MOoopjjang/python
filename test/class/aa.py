#!python3
#-*- coding:utf-8 -*-


class A:
	def __init__( self , _name ):
		self._name = _name


	def __str__( self ):
		return '[%s] name : %s'%(__name__ , self._name)