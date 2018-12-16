#!python3
#-*- coding:utf-8 -*-



import random
import futurist
from futurist import waiters
# from concurrent.futures import ThreadPoolExecutor
# from concurrent.futures import ProcessPoolExecutor



def conpute():
	return sum([random.randint(1,100) for _ in range(1000000)])




def main():

	# ts = None
	with futurist.ThreadPoolExecutor(max_workers = 8) as executors:
		ts = [ executors.submit(conpute) for _ in range(8) ]
		print(executors.statistics)


	results = waiters.wait_for_all(ts)

	# 사용중인 실행자에 관한 통계(statistics)를 제공
	# 작업의 현재 상태를 추적하고 어떻게 코드가 실행되는지에 관한 정보를 얻을때 유용하다.
	print(executors.statistics)

	print('results : {}'.format([ r.result() for r in results.done]))



if __name__ == '__main__':
	main()

