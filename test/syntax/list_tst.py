#!python3
#-*- coding:utf-8 -*-



import os , sys
import copy


LIST_SAMPLE = ['xferlog' , 'kknda' , 'kim' ,'aee' , 'ciek' , 'abc']
LIST_SAMPLE2 = ['kim' , 'park' ,'lee' , 'kim' , 'kim' , 'park']

def test():
	print('LIST_SAMPLE : {}'.format(LIST_SAMPLE))
	print('LIST_SAMPLE2 : {}'.format(LIST_SAMPLE2))
	print('-- index --')
	print('index : {}'.format(LIST_SAMPLE.index('ciek')))
	print('count : {}'.format(LIST_SAMPLE2.count('park')))
	LIST_SAMPLE.sort()
	print('sort LIST_SAMPLE : {}'.format(LIST_SAMPLE))
	LIST_SAMPLE.sort(reverse = True)
	print('reverse LIST_SAMPLE : {}'.format(LIST_SAMPLE))
	LIST_SAMPLE2.remove('lee')
	print('LIST_SAMPLE2 : {}'.format(LIST_SAMPLE2))
	print('-'*20)
	LIST_SAMPLE.extend(set(LIST_SAMPLE2))
	print('LIST_SAMPLE : {}'.format(LIST_SAMPLE))
	print('LIST_SAMPLE : {}'.format(set(LIST_SAMPLE)))
	# ml = list(filter(lambda x:x is not LIST_SAMPLE2, LIST_SAMPLE))
	# print('ml : {}'.format(ml))

# def test2():
# 	v = LIST_SAMPLE & LIST_SAMPLE2
# 	print('v : {}'.format(v))





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
	 test()

	# count_method_tst()

#	extend_method_tst()







