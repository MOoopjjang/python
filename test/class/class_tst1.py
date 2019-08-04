#!python3
#-*- coding:utf-8 -*-





class Person:
	count = 0
	def __init__( self , human_race = 'white' ):
		self._human_race = human_race

	def __str__( self ):
		l = [k+'='+str(v) for k,v in self.__dict__.items()]
		return ','.join(l)




class Cwkim( Person ):
	def __init__(self , human_race , name , age ):
		Person.__init__(self , human_race )
		self._name = name
		self._age = age




#================================================================
#================================================================
#================================================================

from abc import ABCMeta , abstractmethod

class Super(metaclass = ABCMeta):
	def method( self ):
		print('in Super.method')

	def delegate( self ):
		self.action()

	@abstractmethod
	def action( self ):
		assert False , 'action must be defined!'


class Inheritor( Super ):
	pass

class Replacer( Super ):
	def method( self ):
		print('in Replacer.method')
	def action( self):
		print('Replacer.action')

class Extender( Super ):
	def method( self ):
		print('start Extender.method')
		Super.method(self)
		print('end Extender.method')

	def action( self):
		print('Extender.action')


class Provider( Super ):
	# def method( self ):
	# 	print('in Provider.method')
	def action( self ):
		print('Provider action')






if __name__ == '__main__':

	# cwkim = Cwkim('yellow' , 'cwkim' , 20)
	# print(cwkim)

	# b = Cwkim('black' , 'jang' , 40)
	# print(b)

	# cwkim.count = 10
	# print(cwkim.count)
	# print('*'*20)
	# print(cwkim)
	# print(b.count)

	# Person.count = 100
	# print(cwkim.count)
	# print(b.count)



	for kl in [Replacer , Extender , Provider]:
		print(kl.__class__.__name__)
		kl().method()


	p = Provider()
	p.delegate()	

	s = Super()
	s.delegate()
	


