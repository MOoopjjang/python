#!python3
#-*- coding:utf-8 -*-


import threading
import time

# RLOCK

class MyWorker:
	def __init__( self ):
		self.a = 0
		self.b = 0
		self.lock = threading.RLock()


	def modifyA( self ):
		with self.lock:
			for index in range(1 , 100):
				print('modifyA :: RLock._is_owned =>{}'.format(self.lock._is_owned()))
				print('modifyA :: RLock =>{}'.format(self.lock))
				self.a += index
				print('modifyA :: self.a =>{}'.format(self.a))
				time.sleep(5)


	def modifyB( self ):
		with self.lock:
			for index in range(1 , 100):
				print('modifyB :: RLock._is_owned =>{}'.format(self.lock._is_owned()))
				print('modifyB :: RLock =>{}'.format(self.lock))
				self.b += index
				print('modifyB :: self.b =>{}'.format(self.b))
				time.sleep(5)



	def modifyBoth( self ):
		with self.lock:
			print('modifyBoth called ')
			print('{}'.format(self.lock))
			self.modifyA()
			self.modifyB()




if __name__ == '__main__':
	w = MyWorker()
	w.modifyBoth()


