#!python
#-*- coding:utf-8 -*-


registers = {}



def register( obj ):
	registers[obj.__name__] = obj
	return obj

@register
def sam(x):
	return x**2

@register
def ham(x):
	return x**3

@register
class Eggs:
	def __init__( self , x):
		self.data = x**4

	def __str__( self ):
		return str(self.data)


from access2 import accessControl , Private , Public
from rangetest import rangetest


class Person:
	def __init__( self , name , age , _pay ):
		self.name = name
		self.age = age
		self.pay = _pay

	@rangetest([1 , 0.0 , 1.0])
	def giveRaise(self , percent ):
		self.pay = int( self.pay *(1+percent))






# @Private('age')
# class Person:
# 	def __init__( self , age ):
# 		self.age = age

# 	def __add__( self , other ):
# 		self.age += other

# 	def __str__( self ):
# 		return 'Person : '+str(self.age)




if __name__ == '__main__':
	# for name in registers:
	# 	print(name , '=>' , register[name] , type(register[name]))

	sue = Person('kim' , 20 , )














