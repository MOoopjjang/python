#!python
#-*- coding:utf-8 -*-




def func1( func , _limit ):
	l = [func(idx) for idx in range(1,_limit)]
	print('%s'%l)
		



def func2():
	return True , 'xferlog'


def tst_1():
	"""
	반환값이 2개 이상일경우 자동으로 tuple형태로 반환한다.
	"""
	print('안녕하세요~')

	print(r'text \t hi')
	print('text \t hi')


def tst( message , when = None):
	from datetime import datetime
	when = datetime.now() if when is None else when
	print('%s , %s'%(message , when))



def tst_3():
	import sys

	sys.stdout = open('log.txt' , 'w')

	print('xferlog')


def tst_4():
	from decimal import getcontext , Decimal

	getcontext().prec = 3
	result = Decimal(0.1)+Decimal(0.2)
	print(result)

	print(help(result))



if __name__ == '__main__':
	# tst_1()

	# func1(lambda x:x*x , 10)
	# retv = func2()
	# print(type(retv))
	# print(retv[0] , retv[1])

	# tst('hi')

	# tst('hi2' , '2019-x-x-x')


	# tst_3();


	tst_4()


