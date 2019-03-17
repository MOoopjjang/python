#!python
#-*- coding:utf-8 -*-


singletonManager = {}

def singleton(tag='' , dp = False):
	def Wrapped( cls ):
		def onDecorator( *args , **kargv ):
			ninst = False
			if cls not in singletonManager:
				ninst = True
				singletonManager[cls] = cls(*args , **kargv)

			if dp:
				s = 'new' if ninst else 'exist'
				print('[ %s ] is %s instance'%(cls.__name__ , s))
			return singletonManager[cls]
		return onDecorator
	return Wrapped