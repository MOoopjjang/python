#!python3
#-*- coding:utf-8 -*-



def tst2():
	s1 = set([1,2])

	s1.update([3,4,5])
	print('s1 : {}'.format(s1))

	s1.remove(4)
	print('s1 : {}'.format(s1))


def tst1():
	s1 = set([1,2,3])
	s2 = set([3,4,5])
	t1 = set('hello')

	a = s1 | t1
	print('a : {}'.format(a))

	b = s1 & t1
	print('b : {}'.format(b))


	bb = s1 - s2
	print('bb : {}'.format(bb))

	cc = s1^s2
	print('cc : {}'.format(cc))

	aa = s1 | s2
	print('aa : {}'.format(aa))



if __name__ == '__main__':
	# tst1()
	tst2()