#!python3
#-*- coding:utf-8 -*-


import os , sys
import multiprocessing
from concurrent.futures import ProcessPoolExecutor


class MpQueue( multiprocessing.Process ):
	def __init__( self , queue ):
		super( MpQueue , self ).__init__()
		self.queue = queue


	def run( self ):
		print('-- pid : {} --'.format(os.getpid()))
		print(' v : {}'.format(self.queue.get()))



if __name__ == '__main__':
	m = multiprocessing.Manager()
	queue = m.Queue()

	for i in range(10):
		queue.put(i+1)


	# executor = ProcessPoolExecutor(max_workers = 10)

	for i in range(10):
		mq = MpQueue(queue)
		mq.start()
		mq.join()







