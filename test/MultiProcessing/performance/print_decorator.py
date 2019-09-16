#!python3
#-*- coding:utf-8 -*-


import timeit
import psutil


def pdecorator(tag = '' , output = True):
	def onWrapped( func ):
		def onCall( *args , **kargv ):
			start = timeit.default_timer()
			func(*args , **kargv )
			if output:
				print('{}{} duration time : {} -- cpu : {}'.format(tag,func.__name__ , timeit.default_timer() - start, psutil.cpu_percent()) )
		return onCall
	return onWrapped