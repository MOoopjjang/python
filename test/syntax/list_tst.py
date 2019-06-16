#!python3
#-*- coding:utf-8 -*-



import os , sys
import copy

from ps_decorator import cpu_decorator
from ps_decorator import mem_decorator



def test():
	tl = ['xferlog' , 'kknda' ,'aee' , 'ciek' , 'abc']
	strTl = '|'.join(tl)


	tl1 = copy.deepcopy(tl)
	tl2 = tl1[:]
	del tl[1]
	print(tl)
	del tl[:]
	print('tl >>{}'.format(tl))
	print('tl1 >>{}'.format(tl1))
	print('tl2 >>{}'.format(tl2))
	print('strTl >>{}'.format(strTl))


	lllll = [word for word in tl1 if word.startswith('a')]
	print('llll : {}'.format(lllll))


	





if __name__ == '__main__':
	test()


