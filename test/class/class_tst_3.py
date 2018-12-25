#!python3
#-*- coding:utf-8 -*-

# import contains
from contains import Iters


class Person:
	def __init__( self , _name , _age , _addr ):
		self.name = _name
		self.age = _age
		self.addr = _addr


	def __getattr__( self , attrname ):
		if self.name not in self.__dict__:
			return 'Unknown member : {}'.format(attrname)


class Adder:
	def __init__(self , value):
		self.data = value
	def __add__(self , other):
		return self.data+other
	def __radd__( self , other ):
		return self.__add__(other)
	#__radd__ = __add__                             #방법 1



class Callee:
	def __init__( self , value ):
		self.value = value
	def __call__(self , other):
		return self.value * other



class Truth:
	def __bool__( self ):return True




def gen(x):
	for i in range(x):yield i ** 2



def tst_1():
	G = gen(5)
	it = iter(G)
	print(next(it) , next(it))

	print([i for i in gen(5)])


def tst_2():
	X = Iters('xferlog')
	print('X[3] : {}'.format(X[3]))


def tst_3():
	p = Person('xferlog' , 35 , 'incheon')
	print('p.name : {}'.format(p.name))
	print('p.phone : {}'.format(p.phone))



def tst_4():
	a = Adder(10)
	print('a ==> {}'.format(a))
	print('a +10 ==> {}'.format(a+10))
	print('10 + a ==> {}'.format(10+a))


def tst_5():
	C = Callee(10)
	print(' C (4) : {}'.format(C(4)))


def tst_6():
	# cb = (lambda color='yellow':'turn'+color)
	# print(cb('red'))

	X = Truth()
	if X:print('True')




def main():
	# tst_1()

	# tst_2()
	# tst_3()
	
	# tst_4()
	# tst_5()
	tst_6()


if __name__ == '__main__':
	main()




