#!python3
#-*- coding:utf-8 -*-


import os
import random
import threading
import multiprocessing

from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor

# result = []


def func(queue):
	print('-- pid : {} -- '.format( os.getpid()))
	queue.put( sum([random.randint(1,100) for _ in range(100000)]))



def mp_test():
	# result = []
	mgr = multiprocessing.Manager()
	queue = mgr.Queue()
	workers = [ multiprocessing.Process(target = func , args = (queue,)) for _ in range(8)]
	for work in workers:
		work.start()
	for work in workers:
		work.join()

	print('mp_test : result : {}'.format(queue.get()))




def mt_test():
	import queue
	queue = queue.Queue()
	workers  = [ threading.Thread(target = func , args = (queue,)) for _ in range(8)]
	for worker in workers:
		worker.start()
	for worker in workers:
		worker.join()

	print('mt_test : result : {}'.format(queue.get()))



def premi_func():
	return sum([ random.randint(1,100) for _ in range(1000000)])


def premi_mp_test():
	result = None
	with ProcessPoolExecutor(max_workers = 8) as executor:
		futurs = [ executor.submit(premi_func) for _ in range(8) ]


	result = [f.result() for f in futurs]
	print('premi_mp_test result : {}'.format(result))
		

	
def main():
	# mt_test()
	# mp_test()
	premi_mp_test()

if __name__ == '__main__':
	main()



