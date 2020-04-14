#!python3
#-*- coding:utf-8 -*-

# test/book/cookbook




def avg( first , *args ):
	return (first + sum(args))/len(args)


def arg2(first , * , block ):
	print('block : {}'.format(block))



def arg3():
	return 1,2,3,4


def arg4(_x , _y=10):
	'''
		주의 사항 : 함수에 기본인자값을 정의하면  , 값을 바꾸어도 그 이후에 기본값이 변경되지 않는다
		( 함수의 기본값은 함수를 정의할때 생성되므로 , 이후에 변경할수 없다 )
	'''
	print('_x : {} , _y : {}'.format(_x , _y))


def arg5(_x , _y = None):
	if _y is None:
		print('_y is None')

	if _y == None:
		print('_y is None')



def test1():
	'''
	lambda호출시점에 따라 참조하는 x 값이 달라진다. 때문에 익명함수를 사용시 특정변수값을 고정한다 ( 아래코드 : x=x )
	'''
	x = 10
	a = lambda y , x = x:x+y
	x = 20
	b = lambda y , x = x:x+y
	print('a : {}'.format(a(10)))  # 20
	print('b : {}'.format(b(10)))  # 30

	print('-'*20)
	func = [lambda x:x+n for n in range(5)]
	for f in func:
		print(f(0))


def functools_tst():
	'''
	함수에 사용되는 인자값을 고정할수 있으며 , 많은 인지를 넘길경우 ( 실제 인자수를 초과하여 인자를 넘길경우...) 인자수를 줄일수 있다.
	'''
	from functools import partial

	def t(a , b , c , d):
		print(a,b,c,d)

	s1 = partial(t , 1) # a=1
	s1(2,3,4)
	s2 = partial(t , d=10) # d=10
	s2(2,3,4)

	s3 = partial(t , 1 , 2 , d=5) # a = 1 , b = 2 , d = 5
	s3(8)
	s3(8,8)



def funtools_tst_1():
	from functools import partial

	# f = lambda x,y=y:x+y

	def func(x , y):
		return (lambda x:x+y)(x)

	s = partial(func ,y=10)
	print('s1 : {}'.format(s(2)))
		


def functools_tst_mp():
	'''
	funtools.partail 응용 
	'''
	from functools import partial
	from multiprocessing import Pool
	import logging

	def output_result( result , log = None):
		if log is not None:
			log.debug('Got : %r',result)


	def add( a , b ):
		return a+b

	logging.basicConfig(level = logging.DEBUG )
	log = logging.getLogger(' test ')

	p = Pool()
	p.apply_async( add , (3,4) , callback = partial(output_result , log = log))
	# p.close()
	p.join()
	











if __name__ == '__main__':
	# print('{}'.format(avg(2,1,2,3,4)))

	# arg2(2  , block=4 )

	# r1,_,*r3 = arg3()
	# print('r1:{} , r3:{}'.format(r1 , r3))
	# print('result : {}'.format(arg3()))


	# arg4(2)
	# arg4(1,23)

	# arg5(10)
	# arg5(10,3)


	# test1()
	# functools_tst()

	# functools_tst_mp()

	funtools_tst_1()

