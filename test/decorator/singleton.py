#!python3
#-*- coding:utf-8 -*-


manager = {}

def singleton( cls ):
	def onCalled( *args , **kargv ):
		obj = None
		if cls not in manager:
			print('%s create'%(cls.__name__))
			manager[cls] = cls(*args , **kargv )
		return manager[cls]
	return onCalled


def singleton2( cls ):
	def onCalled( *args , **kargv ):
		if onCalled.instances == None:
			print('%s create'%(cls.__name__))
			onCalled.instances = cls( *args , **kargv )
		return onCalled.instances
	onCalled.instances = None
	return onCalled


class singleton3:
	def __init__( self , aClass):
		self.aClass = aClass
		self.instance = None

	def __call__( self , *args , **kargv ):
		if self.instance == None:
			print('%s create'%(self.aClass.__name__))
			self.instance = self.aClass( *args , **kargv )
		return self.instance



# @singleton
# @singleton2
@singleton3
class Person:
	def __init__( self , name , age ):
		self.name = name
		self.age = age


if __name__ == '__main__':
	p = Person('xferlog' , 20)
	pp = Person('kknda' , 30)


	