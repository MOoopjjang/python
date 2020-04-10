#!python3
#-*- coding:utf-8 -*-

import multiprocessing
import time
import cotyledon


"""
   cotyledon을 이용한 background process 실행
   - queue를 이용한 data 공유
"""


class MManager( cotyledon.ServiceManager ):
	def __init__( self ):
		cotyledon.ServiceManager.__init__( self )
		self.queue = multiprocessing.Manager().Queue()
		self.add(Producer , args = (self.queue , ))
		self.add(Consumer , args = (self.queue , ),workers = 2)




class Producer( cotyledon.Service ):
	def __init__( self ,worker_id, _queue ):
		cotyledon.Service.__init__( self , worker_id)
		self._queue = _queue


	def run( self ):
		count = 0
		while True:
			self._queue.put(count)
			count+=1
			time.sleep(4)




class Consumer( cotyledon.Service ):
	def __init__( self ,worker_id ,_queue):
		cotyledon.Service.__init__( self , worker_id)
		self._queue = _queue
		self._worker_id = worker_id

	def run( self ):
		while True:
			j = self._queue.get(block = True)
			print("I am worker :: id : {} , pid : {} , job : {}".format(self._worker_id , self.pid , j))
			time.sleep(1)




if __name__ == '__main__':
	MManager().run()


