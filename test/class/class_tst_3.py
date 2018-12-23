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


def main():
	# tst_1()

	# tst_2()
	tst_3()
	



if __name__ == '__main__':
	main()