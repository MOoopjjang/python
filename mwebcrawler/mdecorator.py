#!python
#-*- coding:utf-8 -*-


"""
  start_end_loging : paramer값을 출력해주는 decorator
"""


def start_end_loging(tag = '' , db = False):
	def onDecorator( func ):
		def onCall( *args , **kargv ):
			if db: print('[%s][%s] start :: args : %s \n\t kargs : %s'%(tag , func.__name__ , args , kargv))
			result = func(*args , **kargv)
			if db: print('[%s][%s] end :: '%(tag , func.__name__))
			return result
		return onCall
	return onDecorator