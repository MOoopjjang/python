#!python3
#-*- coding:utf-8 -*-



def tst_1():
	s = {1}
	print(type(s))

	print('s : {}'.format(s))
	print('s.pop() : {}'.format(s.pop()))
	print('s : {}'.format(s))


def add(a,b):
	return a+b

def tst_2():
	from functools import reduce

	nums = [1,10,-1,32,2,12,67]

	r = reduce(add , nums)
	print('result : {}'.format(r))


def tst_3():
	names = ['xfelog' , 'kknda' , 'cwkim' , 'zang' , 'kang']

	s = sorted(names , key = lambda w:w , reverse = True)
	print('s : {}'.format(s))


def tst_4():
	





if __name__ == '__main__':
	# tst_1()

	# tst_2()

	tst_3()