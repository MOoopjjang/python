#!python3
#-*- coding:utf-8 -*-



import os , sys
import copy

from ps_decorator import cpu_decorator
from ps_decorator import mem_decorator

LIST_SAMPLE = ['xferlog' , 'kknda' ,'aee' , 'ciek' , 'abc']
LIST_SAMPLE2 = ['kim' , 'park' ,'lee' , 'kim' , 'kim' , 'park']

def test():
	print('*'*10+'LIST_SAMPLE'+'*'*10)
	print(LIST_SAMPLE)

	print('*'*10+'deep copy'+'*'*10)
	copy_list = LIST_SAMPLE[:]
	print('copy_list : {}'.format(copy_list))

	print('*'*10+'copy_list remove'+'*'*10)
	del copy_list[1]
	print(LIST_SAMPLE)
	print('copy_list : {}'.format(copy_list))
	copy_list.remove('ciek')
	print('copy_list : {}'.format(copy_list))

	fl=[ v for v in LIST_SAMPLE if v.startswith('a') ]
	print(fl)

	print('*'*10+'LIST_SAMPLE search'+'*'*10)
	print(LIST_SAMPLE.index('kknda'))

	print('*'*10+'copy_list insert'+'*'*10)
	print('copy_list : {}'.format(copy_list))
	copy_list.insert(1 , 'add_1')
	print('copy_list : {}'.format(copy_list))

	print('*'*10+'copy_list sort'+'*'*10)
	copy_list.sort()
	print(copy_list)
	copy_list.sort(reverse = True)
	print(copy_list)



def count_method_tst():
	# count
	while True:
		for sample in LIST_SAMPLE2:print('{}'.format(sample))
		count_str = input('input item :')
		if count_str == 'q':break
		count = LIST_SAMPLE2.count(count_str)
		print(count_str+' count : {}'.format(count))

	
def extend_method_tst():
	LIST_SAMPLE.extend(['1','2','3'])
	print('LIST_SAMPLE : {}'.format(LIST_SAMPLE))






if __name__ == '__main__':
	# test()

	# count_method_tst()

	extend_method_tst()







