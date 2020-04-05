#!python3
#-*- coding:utf-8 -*-


class Super:
	def hello( self ):
		self.data1 = 'hello'



class Sub( Super ):
	def holla( self ):
		self.data2 = 'holla'



if __name__ == '__main__':
	X = Sub()
	print('X -- {}'.format(X.__dict__))
	X.hello()
	print('X- hello -- {}'.format(X.__dict__))
	X.holla()
	print('X- hello- holla -- {}'.format(X.__dict__))

	print('-'*20)

	print('X.__dict__[\'holla\'] :: {}'.format(X.__dict__['holla']))
	print('X.__dict__[\'data1\'] :: {}'.format(X.__dict__['data1']))
