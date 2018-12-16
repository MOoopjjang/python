#!python3
#-*- coding:utf-8 -*-


import time
import multiprocessing
import cotyledon

"""
  cotyledon을 이용한 bg process를 생성 
  - kill -HUP pid 를 통해 reload 호출
"""

class Manager( cotyledon.ServiceManager ):
	def __init__( self ):
		super( Manager , self ).__init__()
		self.queue = multiprocessing.Manager().Queue()
		self.add( Producer , args = ( self.queue ,))
		self.consumer = self.add( Consumer , args = ( self.queue ,) , workers = 2)
		self.register_hooks( on_reload = self.reload )


	def reload( self ):
		print('reloading...')
		self.reconfigure( self.consumer , 5)




class Producer( cotyledon.Service ):
	def __init__( self , worker_id , queue ):
		super( Producer , self ).__init__( worker_id )
		self.queue = queue

	def run( self ):
		count = 0
		while True:
			self.queue.put(count)
			time.sleep(1)
			count +=1



class Consumer( cotyledon.Service ):
	def __init__( self , worker_id , queue ):
		super( Consumer , self ).__init__( worker_id )
		self.queue = queue
		

	def run ( self ):
		while True:
			j = self.queue.get( block = True )
			print('pid : {} , wid : {} , job : {}'.format(self.pid , self.worker_id , j))




if __name__ == '__main__':
	Manager().run()









