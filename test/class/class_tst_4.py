#!python3
#-*- coding:utf-8 -*-

from display.listinstance import ListInstance

def square( arg ):
	return arg ** 2


class base:
	def __init__( self ):pass

	def __repr__( self ):
		l = [ '{}={}'.format(k,v) for k,v in self.__dict__.items()]
		output = ','.join(l)
		return '[{} ]: {}'.format( self.__class__.__name__, output)



class child( base ):
	def __init__( self ):
		base.__init__( self)
		self.name = 'xferlog'
		self.age = 20



class Sum:
	def __init__( self , num ):
		self.num = num
	def __call__( self  , arg ):
		return self.num + arg


class Product( ListInstance ):
	def __init__( self , val):
		self.val = val
	def method(self , arg):
		return self.val * arg


def main():

	# s = Sum(3)
	# p = Product(5)
	# action_ar = [ square , s , p.method ]
	# for func in action_ar:print('{}'.format(func(4)))
	# r = [ func(3) for func in action_ar]
	# print('r : {}'.format(r))

	# r1 = list(map(lambda x:x(3) , action_ar))
	# print('r1 : {}'.format(r1))

	# print(action_ar[-1](5))


	# c = child()
	# print(c)


	p = Product(10)
	print(p)



if __name__ == '__main__':
	main()