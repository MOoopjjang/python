#!python3
#-*- coding:utf-8 -*-


import time , timeit
import itertools
import random
import psutil
import os


def sleep_func( x ):
	print('sleep...')
	time.sleep(1)
	return x


def gen():
	g = (sleep_func(i) for i in range(5))
	for gg in g:
		print('gg : {}'.format(gg))


def normal():
	ll = [sleep_func(i) for i in range(5)]
	for l in ll:
		print('l : {}'.format(l))



def fib():
	print('step - 1')
	prev,curr=0,1
	print('step - 2')
	while True:
		print('step - 3')
		yield curr
		print('step - 4')
		prev , curr = curr , prev + curr


def square_numbers( x ):
	for i in x:
		yield i*i




names = ['cwkim' , 'bhkim' , 'khlee' , 'kjk' , 'kmk']
ages = [42,45,40,27,34]



def n_list( x ):
	result = []
	for i in range(x):
		info = {}
		info['id'] = i
		info['name'] = random.choice(names)
		info['age'] = random.choice(ages)

		result.append(info)

	return result



def n_generator( x ):
	for i in range(x):
		info = {}
		info['id'] = i
		info['name'] = random.choice(names)
		info['age'] = random.choice(ages)

		yield info




def n_caller():
	process = psutil.Process(os.getpid())
	mem_before = process.memory_info().rss/1024/1024

	start = timeit.default_timer()
	nlist = n_list(1000000)

	mem_after = process.memory_info().rss/1024/1024
	print(' mem_before : {}'.format(mem_before))
	print(' mem_after : {}'.format(mem_after))
	print(' time : {}'.format(timeit.default_timer() - start))


def g_caller():
	process = psutil.Process(os.getpid())
	mem_before = process.memory_info().rss/1024/1024

	start = timeit.default_timer()
	nlist = n_generator(1000000)

	mem_after = process.memory_info().rss/1024/1024
	print(' mem_before : {}'.format(mem_before))
	print(' mem_after : {}'.format(mem_after))
	print(' time : {}'.format(timeit.default_timer() - start))





if __name__ == '__main__':
	# normal()
	# gen()

	# f = fib()
	# ll = list(itertools.islice(f , 0 , 10))


	# for xx in square_numbers([1,2,3,4,5,6,7,8,9,10]):
	# 	print('xx : {}'.format(xx))


	# n_caller()
	g_caller()


 













