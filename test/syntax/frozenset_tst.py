#!python3
#-*- coding:utf-8 -*-



def tst_1():

	fs = frozenset(['a' , 'b' , 'c'])
	print(fs)
	# fs.add('1')


if __name__ == '__main__':
	func = tst_1


	print(func.__name__)
	print(func.__doc__)
	print(func.__globals__)
	print(func.__dict__)



