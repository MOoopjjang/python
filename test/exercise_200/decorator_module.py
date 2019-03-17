#!python
#-*- coding:utf-8 -*-




def print_decorator(tag = '' , dp = False):
	def Wrapped( func ):
		def onCall( *args ):
			result = func(*args)
			if dp:
				print('[%s] args : %s '%(tag , args))
			return result

		return onCall
	return Wrapped
