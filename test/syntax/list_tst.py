#!python3
#-*- coding:utf-8 -*-



import os , sys
import copy


LIST_SAMPLE = ['xferlog' , 'kknda' , 'kim' ,'aee' , 'ciek' , 'abc' , 'ciek']
LIST_SAMPLE2 = ['kim' , 'park' ,'lee' , 'kim' , 'kim' , 'park']

def test():
	print("{}".format(LIST_SAMPLE2.index("lee")))
	print("-"*30)
	count = LIST_SAMPLE.count('ciek')
	print('count : {}'.format(count))
	print("-"*30)
	index = LIST_SAMPLE.index("aee")
	print(f'index : {index}')
	print("-"*30)
	LIST_SAMPLE.extend(LIST_SAMPLE2)
	print(f'LIST_SAMPLE: {LIST_SAMPLE}')
	print("-"*30)
	LIST_SAMPLE2.append('1')
	print(f'LIST_SAMPLE2: {LIST_SAMPLE2}')
	LIST_SAMPLE2.remove("kim")
	print(f'LIST_SAMPLE2: {LIST_SAMPLE2}')

	LIST_SAMPLE.insert(2 , "ejkim")
	print(f'LIST_SAMPLE: {LIST_SAMPLE}')


def test2():
	rlist = LIST_SAMPLE[::-1]
	print(f'LIST_SAMPLE : {LIST_SAMPLE}')
	print(f'rlist : {rlist}')

	LIST_SAMPLE[3] = "ddddd"
	print(f'LIST_SAMPLE : {LIST_SAMPLE}')
	del LIST_SAMPLE[3]
	print(f'LIST_SAMPLE : {LIST_SAMPLE}')


def test3():
	for i in range(10):
		print(f'{i}')

	ll = [ i+10 for i in range(10) ]
	print(f'{ll}')


def test4():
	LIST_SAMPLE.sort()
	print(f'sList : {LIST_SAMPLE}')
	LIST_SAMPLE.sort(reverse = True)
	print(f'sList : {LIST_SAMPLE}')
	ssl = sorted(LIST_SAMPLE , reverse = False)
	print(f'ssl : {ssl}')


def exam_cat_name_list():
	l = []
	while True:
		catName = input('Name:')
		if catName == '' or catName == None:
			break
		if catName not in l:
			l.append(catName)
	print(f'{l}')




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
	 # test()
	 # test2()
	 # test3()
	 test4()

	# count_method_tst()
#	extend_method_tst()
	# cat_exam()







