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


if __name__ == '__main__':
	# tst_1()

	# func1(lambda x:x*x , 10)
	retv = func2()
	print(type(retv))
	print(retv[0] , retv[1])
