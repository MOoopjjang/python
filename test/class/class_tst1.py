#!python3
#-*- coding:utf-8 -*-




from abc import ABCMeta , abstractmethod


# 3.x
class Base( metaclass = ABCMeta ):
	# __metaclass__ = ABCMeta   # 2.x

	def __init__( self  , kind ):  
		self._kind = kind

	def __str__( self ):
		return '[kind] %s'%(self._kind)

	@abstractmethod
	def getName( self ):
		pass
		

	def getInfo( self ):
		return "info"



class Human( Base ):
	def __init__( self ):
		Base.__init__( self , 'Human')

	def getInfo( self ):
		return 'human info'

	def getName( self ):
		return 'cwkim'



class Undeaded( Base ):
	def __init__( self ):
		Base.__init__( self , 'undeaded')




class MNumber:
	def __init__( self , v ):
		self._value = v


	def __add__(self , value):
		return self._value + value

	def __sub__( self , value ):
		return self._value - value









if __name__ == '__main__':

	# base = Base('a')
	# print('Base : {}'.format(base))

	# human = Human()
	# print('human : {} , {}'.format(human , human.getName()))

	# undeaded = Undeaded()
	# print('undeaded : {} , {}'.format(undeaded , undeaded.getName()))


	n = MNumber(10)
	print('+ : {}'.format(n+10))
	print('- : {}'.format(n-2))
	n+=2
	print('n+=2 : {}'.format(n))

	n-=2
	print('n-=2 : {}'.format(n))





	


