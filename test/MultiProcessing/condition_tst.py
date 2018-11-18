#!python3
# -*- coding:utf-8 -*-



import threading
import time , random


class Publish( threading.Thread ):
	def __init__( self , _condition , _integers ):
		self.condition = _condition
		self.integers = _integers
		threading.Thread.__init__( self )

	def run( self ):
		print('Publish start ---')
		while True:
			print('Publish acquire')
			self.condition.acquire()
			v = random.randint(0 , 100)
			self.integers.append(v)
			print('Publish value : {}'.format(v))
			print('Publish notify')
			self.condition.notify()
			self.condition.release()
			time.sleep(1)



class Subscribe( threading.Thread ):
	def __init__( self , _condition , _integers ):
		self.condition = _condition
		self.integers = _integers
		threading.Thread.__init__( self )

	def run( self ):
		print('Subscribe start ---')
		
		while True:
			self.condition.acquire()
			print('Subscribe acquire')
			while True:
				if self.integers:
					v = self.integers.pop()
					print('Subscribe pop : {}'.format(v))
					break
				print('Subscribe waiting...')
				self.condition.wait()
			print('Subscribe release')
			self.condition.release()




if __name__ == '__main__':

	# 발행자
	integers = []
	condition = threading.Condition()
	publish = Publish( condition , integers )
	publish.start()


	# 구독자
	consumer_1 = Subscribe( condition , integers )
	consumer_2 = Subscribe( condition , integers )
	consumer_1.start()
	consumer_2.start()

	# Join
	publish.join()
	consumer_1.join()
	consumer_2.join()
	















