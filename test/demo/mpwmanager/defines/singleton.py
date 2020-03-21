#!python3
#-*- coding:utf-8 -*-


singletonlist = {}

def Singleton(tag = '' , display = False ):
	def Wrapped( cls ):
			def onDecorator( *args , **kargv ):
				if cls not in singletonlist:
					singletonlist[cls] = cls( *args , **kargv )

					if display:
						print('{} '.format(cls.__name__ ))
				return singletonlist[cls]
			return onDecorator
	return Wrapped