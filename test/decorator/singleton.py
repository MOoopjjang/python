#!python
#-*- coding:utf-8 -*-



instances = {}



def singleton( cls ):
	def onCall( *args , **kargs ):
		# print('%s'%instances)
		if cls.__name__ not in instances:
			print('n = %s - args : %s  - kargs : %s'%(cls.__name__ , args , kargs))
			inst = cls(*args , **kargs)
			instances[cls.__name__] = inst
			return inst
		return instances[cls.__name__]
	return onCall



@singleton
class Person:
	def __init__( self , name , age):
		self.name = name
		self.age = age






if __name__ == '__main__':
	p1 = Person('xferlog' , 20)
	print('n : %s - a : %s'%(p1.name , p1.age))

	p2 = Person('kknda' , 21)
	print('n : %s - a : %s'%(p2.name , p2.age))
