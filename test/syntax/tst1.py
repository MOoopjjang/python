#!python
#-*- coding:utf-8 -*-




def func1( func , _limit ):
	l = [func(idx) for idx in range(1,_limit)]
	print('%s'%l)
		


def tst_1():
	print('안녕하세요~')

	print(r'text \t hi')
	print('text \t hi')


if __name__ == '__main__':
	# tst_1()

	func1(lambda x:x*x , 10)
