#!python3
#-*- coding:utf-8 -*-


attrs = []

class ClassTools:
	def _getAttrs( self ):
		for k in self.__dict__:
			attrs.append('{}={}'.format(k , getattr(self , k)))
		return ','.join(attrs)
