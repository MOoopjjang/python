#!python3
#-*- coding:utf-8 -*-




import random
import futurist
import timeit
import queue
#from __future__ import print_function
import psutil
import multiprocessing
import os , sys

"""
  - java의 multi threading vs python multi threading vs Python Processing
    의 performance를 비교하기 위한 예제 소스

  - result :
     mp_performance_2_result.txt

"""

queue = queue.Queue()

def compute(_queue):
	_queue.put(sum([ random.randint(0,100) for _ in range(1000000) ]))


def resource_info(_startTime):
	print('CPU usage : {}'.format(psutil.cpu_percent()))
	print('consume time : {}'.format(timeit.default_timer() - _startTime))
	


def mp_test():
	qu = multiprocessing.Manager().Queue()
	startTime = timeit.default_timer()
	with futurist.ProcessPoolExecutor( max_workers = 8 ) as executors:
		futures = [executors.submit(compute , qu) for _ in range( 8 )]
		results = [f.result() for f in futures]

		print('result : {}'.format(qu.get()))
		resource_info(startTime)
		


def mt_test():
	startTime = timeit.default_timer()
	with futurist.ThreadPoolExecutor( max_workers = 8 ) as executors:
		futures = [ executors.submit(compute ,queue) for _ in range( 8 ) ]
		results = [f.result() for f in futures]

		print('result : {}'.format(queue.get()))
		resource_info(startTime)




def main():
	print('argv : {}'.format(sys.argv))
	if sys.argv[1] == '1':
		mt_test()
	else:
		mp_test()



if __name__ == '__main__':
	main()

