#!python3
#-*- coding:utf-8 -*-



import os , sys
import copy

from ps_decorator import cpu_decorator
from ps_decorator import mem_decorator


@mem_decorator
def test():
	ar = ['xferlog' , 'akdladlf' , 'bhkim']
	arr = [len(a) for a in ar]
	for n in arr:print('n : {}'.format(n))

@mem_decorator
def gen_test():
	ar = ['xferlog' , 'akdladlf' , 'bhkim']
	arr = (len(a) for a in ar)
	for n in arr:print('n : {}'.format(n))


def test4():
	ar = [['x' , 'f' , 'e'],['a','b','c']]

	print('ar : {}'.format(ar))
	v = [ x for row in ar for x in row]
	print('v ; {}'.format(v))

	arr = [1,2,3,4,5,6,7,8,9,10]

	vv = [ v for v in arr if v>4 if v%2 == 0 ]
	print('vv ; {}'.format(vv))




def test3():

	tt = [1,2,3,4,5,6]
	ps = [ t**2 for t in tt ]
	print(ps)

	print('-'*20)
	psss = list(map(lambda x:x**2 , tt))
	print('map : {}'.format(psss))
	print('-'*20)
	a = [ x**2 for x in tt if x%2 == 0]
	print('a : {}'.format(a)) 

	b = list(map(lambda x:x**2 , filter(lambda xx:xx%2 == 0 , tt)))
	print('b : {}'.format(b))

def test2():
	tl = ['a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h']
	print(tl[2:-2])

	print('t1 : {}'.format(tl))
	t2 = tl[:]
	print('t2 : {}'.format(t2))
	t2[2:4] = [10]

	print('t1 : {}'.format(tl))
	print('t2 : {}'.format(t2))




def test1():
	spam = ['xferlog' , 'kknda' , 'bhkim' , 'ejkim']
	print(spam)
	del spam[2]
	print(spam)

	if 'ejkim'  not in spam:
		print('exist!')


	a , b , c = spam
	print(a+':'+b+':'+c)	

	print(spam.index('kknda'))

	spam.insert(2,'ccccc')
	print(spam)

	sssss = 'xferlog hi how are you?'
	bhss = sssss.replace('kcwda' , 'bhkim')
	print(sssss)
	# ssl = list(sssss)
	# ssl.replace('kcwda' , 'bhkim')
	

	print(bhss)

	list_ss = list(sssss)
	list_ss[:len('xferlog')] = 'bhkim'
	convert_str = ''.join(list_ss)
	print(convert_str)

	t_l_s = tuple(list_ss)
	print(t_l_s)
	l_t_s = list(t_l_s[0:len('bhkim')])
	print(l_t_s)

	tt = ('xferlog',)
	print(type(tt))

	bl = ['kknda' , 'bhkim']
	cl = copy.deepcopy(bl)
	cl[0]='kkk'
	print(bl)
	print(cl)




if __name__ == '__main__':
	test()


