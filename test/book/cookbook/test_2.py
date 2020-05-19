#!python3
#-*- coding:utf-8 -*-



'''
단일 메소드를 제공하는 class를 method로 변경
'''

class One:
	'''
	AS-IS
	'''
	def __init__(  self , _name ):
		self._name = _name

	def getName( self ):
		return self._name



def MOne(_name):
	name = _name
	def getName(**kargv):
		return name





if __name__ =='__main__':
	o = One('xferlog')
	print('{name}'.format(name=o.getName()))

	print('*'*20)
	o2 = MOne('cwkim')
	print('{name}'.format(o2.getName()))