#!python3
#-*- coding:utf-8 -*-


import psutil

def cpu_decorator( func ):
	def onDecorator( *args , **kargv ):
		print('[ %s ] cpu before : %s'%(func.__name__ , psutil.cpu_percent()))
		r = func(*args , **kargv )
		print('[ %s ] cpu after : %s'%(func.__name__ , psutil.cpu_percent()))
		return r
	return onDecorator



def mem_decorator( func ):
	def onDecorator( *args , **kargv ):
		v_info = psutil.virtual_memory()
		print('[ %s ] mem before : %s'%(func.__name__ , v_info.used))
		r = func(*args , **kargv )
		print('[ %s ] mem after : %s'%(func.__name__ , v_info.used))
		return r
	return onDecorator