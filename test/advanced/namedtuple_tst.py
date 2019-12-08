#!python
#-*- coding:utf -*-


from collections import namedtuple

stock = namedtuple('stock' , ['name' , 'shares' , 'price'])

def compute_cost( recoreds ):
	total = 0.0
	for rec in records:
		s = stock(*rec)
		total += s.shares * s.price


def tst_2():
	ar = []
	ar.append(stock('kcwda' , 100 , 123.45))
	ar.append(stock('bhkim' , 50 , 45.12))
	ar.append(stock('ejkim' , 110 , 542.1))

	v = max(ar , key = lambda x:x.shares)
	print('v : {}'.format(v))


def tst_1():
	'''
		- 이름으로 접근가능
		- db로 부터 데이타륿 받아서 정재시 유용
	'''
	from collections import namedtuple

	subscriber = namedtuple('subscriber' , ['addr' , 'joined'])
	sub = subscriber('jonesy@example.com' , '2012-10-19')
	print('sub : {}'.format(sub))

	print('sub.addr : {}'.format(sub.addr))
	print('sub.joined : {}'.format(sub.joined))


if __name__ == '__main__':
	# tst_1()

	tst_2()



