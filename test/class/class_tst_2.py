#!python3
#-*- coding:utf-8 -*-


class Super:
	def hello( self ):
		self.data1 = 'spam'


class Sub ( Super ):
	def hola( self ):
		self.data2 = 'eggs'


if __name__ == '__main__':
	X = Sub()
	print(X.__dict__)
	print(X.__class__)
	print(Sub.__bases__)
	print(Super.__bases__)

	Y = Sub()
	print(X.hello())
	print('X.__dict__ : {}'.format(X.__dict__))

	X.hola()
	print('X.__dict__ : {}'.format(X.__dict__))

	l = list(Sub.__dict__.keys())
	print(l)