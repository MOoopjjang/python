#!python3
#-*- coding:utf-8 -*-



#Condition
# 다른 스레드의 신호를 기다리는 동기화 프리미티브.


import threading
import random

class Publisher( threading.Thread ):
	def __init__( self , integers , condition):
		self.integers = integers
		self.condition = condition
		threading.Thread.__init__( self )

	def run( self ):
		integer = random.randint(0 , 1000)
		self.condition.acquire()
		print('Condition Acquired by Publisher : {}'.format(self.name))
		self.integers.append(integer)
		self.condition.notify()
		print('Condition Released by Publisher : {}'.format(self.name))
		self.condition.release()
		time.sleep(1)


class Subscriber( threading.Thread ):
	def __init__( self , integers , condition ):
		self.integers = integers
		self.condition = condition
		threading.Thread.__init__( self )

	def run( self ):
		while True:
			self.condition.acquire()
			print('Condition Acquired by Consumer : {}'.format(self.name))
			while True:
				if self.integers:
					integer = self.integers.pop()
					print('{} Popped from list by Consumer: {}'.format(integer , self.name))
					break
				print('Condition Wait by {}'.format(self.name))
				self.condition.wait()
			print('Consumer {} Releasing Condition'.format(self.name))
			self.condition.release()




def main():
	integers = []
	condition = threading.Condition()
	# 발행자
	pub1 = Publisher(integers , condition )
	pub1.start()

	#구독자
	sub1 = Subscriber(integers , condition)
	sub2 = Subscriber(integers , condition)
	sub1.start()
	sub2.start()
	# 스레드 조인
	pub1.join()
	consumer1.join()
	consumer2.join()




if __name__ == '__main__':
	main()











