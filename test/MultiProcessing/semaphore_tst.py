#!python3
# -*- coding:utf-8 -*-


import threading
import time , random

class TicketSeller( threading.Thread ):
	ticketsSold = 0
	def __init__( self , _semaphore ):
		self.sem = _semaphore
		threading.Thread.__init__( self )

	def run( self ):
		global ticketsAvailable
		running = True
		while running:
			self.randomDelay()
			self.sem.acquire()
			if( ticketsAvailable <= 0 ):
				running = False
			else:
				self.ticketsSold = self.ticketsSold+1
				ticketsAvailable = ticketsAvailable - 1
				print('{} Sold One({} left)'.format(self.getName() , ticketsAvailable))
			self.sem.release()
		print('Ticket Seller {} Sold {} tickets in total'.format(self.getName() , self.ticketsSold))
	def randomDelay( self ):
		time.sleep(random.randint(0,1))



if __name__ == '__main__':
	semphore = threading.Semaphore()

	# 티켓 할당
	ticketsAvailable = 10

	# 배열 생성
	sellers = []
	for i in range(0,4):
		seller = TicketSeller( semphore )
		seller.start()
		sellers.append( seller )

	for s in sellers:
		s.join()
