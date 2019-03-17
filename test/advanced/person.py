#!python3
#-*- coding:utf-8 -*-

from classtools import AttrDisplay
from rangetest import rangetest

class Person ( AttrDisplay ):
	def __init__( self , _name , _job = None , _pay = 0):
		self.name = _name
		self.job = _job
		self.pay = _pay
		AttrDisplay.__init__( self )


	# def __repr__( self ):
	# 	return AttrDisplay.__repr__( self )

	def lastName( self ):
		return self.name.split()[1]

	def giveRaise( self , percent ):
		self.pay = int( self.pay * (1 + percent ))

	# def giveRaise( self , percent ):
	# 	if percent < 0.0 or percent > 1.0:
	# 		raise TypeError('percent invalid')
	# 	self.pay = int( self.pay * (1 + percent ))



if __name__ == '__main__':
	p = Person('bob')
	print(p)