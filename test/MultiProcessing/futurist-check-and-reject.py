#!python3
#-*- coding:utf-8 -*-


import futurist
from futurist import rejection
import random




def compute():
	return sum([ random.randint(0 , 100) for _ in range(1000000)])



def main():
	"""
	check_and_reject로 큐의 크기 제한.
	"""
	with futurist.ThreadPoolExecutor(max_workers = 8 , check_and_reject = rejection.reject_when_reached(2)) as executors:
		futures = [ executors.submit(compute) for _ in range(20)]
		print(' statistics : {}'.format(executors.statistics))

	results = [ f.result() for f in futures]
	print(' statistics : {}'.format(executors.statistics))
	print('result : {}'.format(results))




if __name__ == '__main__':
	main()