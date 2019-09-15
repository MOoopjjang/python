#!python
#-*- coding:utf-8 -*-


import time
import threading
from threading import Thread

def threadWorker():
	print('####### threadWorker Start #####')
	time.sleep(10)
	print('####### threadWorker End #######')

	print('enumerate () : {}'.format(threading.enumerate()))
	print('active_count () : {}'.format(threading.active_count()))



def daemonThread():
	# print('####### Daemon Thread Start #######')
	while True:
		print('####### Daemon Thread Start : {} #######'.format(threading.current_thread()))
		print('active_count : {}'.format(threading.active_count()))
		time.sleep(2)
	print('####### Daemon Thread End #######')



def tst_1():
	print('{}'.format(threading.main_thread()))

	nThread = Thread(target = threadWorker)
	dThread = Thread(target = daemonThread)

	dThread.setDaemon(True)

	dThread.start()
	nThread.start()

	print('####### main end #######')




def sample_func(_i):
	print('##### {} start #####'.format(threading.current_thread()))
	print('##### {} start #####'.format(threading.enumerate()))
	time.sleep(_i * 2)
	print('##### {} end #####'.format(threading.current_thread()))
	return _i*2


def tst_2():
	import concurrent.futures
	from concurrent.futures import ThreadPoolExecutor

	with ThreadPoolExecutor(max_workers = 2) as executor:
		tasks = [ executor.submit(sample_func , i) for i in range(1,3)]

		for task in tasks:
			print('result : {}'.format(task.result()))

			

def tst_3():
	



if __name__ == '__main__':

	# tst_1()

	tst_2()


	





	
