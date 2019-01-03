#!python3
#-*- coding:utf-8 -*-

import multiprocessing
import time
import cotyledon


"""
   cotyledon을 이용한 background process 실행
   - queue를 이용한 data 공유
"""


class Manager( cotyledon.ServiceManager ):
	def __init__( self  ):
		super(Manager , self).__init__()
		self.queue = multiprocessing.Manager().Queue()
		self.add(ProducerService , args = (self.queue,))
		self.add(ConsumerService , args=(self.queue,) , workers = 2)




class ProducerService( cotyledon.Service ):
	def __init__( self , worker_id , queue ):
		super( ProducerService , self ).__init__(worker_id)
		self.queue = queue

	def run( self ):
		i = 0
		while True:
			self.queue.put(i)
			time.sleep(1)
			i +=1



class ConsumerService( cotyledon.Service ):
	def __init__( self , worker_id , queue ):
		super( ConsumerService , self ).__init__(worker_id)
		self.queue = queue


	def run( self ):
		while True:
			j = self.queue.get(block = True)
			print('pid : {} , worker_id : {} , job : {}'.format(self.pid , self.worker_id , j))



if __name__ == '__main__':
	Manager().run()


