#!python
#-*- coding:utf-8 -*-


def rfwd( path = 'billboard.json' , mode = False):
	def onWrapped( func ):
		def onDecorator(*args , **kargv ):
			r = func(*args , **kargv )
			if mode:
				import json
				with open(path , 'w') as fw:
					json.dump(r , fw)
			return r
		return onDecorator
	return onWrapped