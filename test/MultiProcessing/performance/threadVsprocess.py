#!python3
#-*- coding:utf-8 -*-



import os
import timeit
import time
from threading import Thread
from multiprocessing import Process





def func():
	print('#'*10+'myfunc'+'#'*10)
	time.sleep(2)


def tst1():
	"""
	thread와 process의 생성시간 비교
     - thread : 0.001929684000000001
     - process : 0.022118336999999766
	"""

	t1 = timeit.default_timer()


	threads = []
	for _ in range(10):
		t = Thread(target = func)
		t.start()
		threads.append(t)

	print('Thread 10 Create Duration Time  : {}'.format(timeit.default_timer() - t1))

	for thread in threads:thread.join()

	t1 = timeit.default_timer()
	procs = []
	for _ in range(10):
		p = Process(target = func)
		p.start()
		procs.append(p)

	print('Process 10 Create Duration Time  : {}'.format(timeit.default_timer() - t1))
	for proc in procs:proc.join()

	print('End!!')







if __name__ == '__main__':
	tst1()
