#!python3
#-*- coding:utf-8 -*-



def weakrefTst():
	'''
	약한 참조 테스트
	'''
	import weakref
	import time

	a_set = {0,1}
	wref = weakref.ref(a_set)
	print('{}'.format(wref))
	print('wref > {}'.format(wref()))
	a_set = {2,3}
	while wref() is not None:
		print(wref() is None)
		time.sleep(1)

	print('end')


def copyTst():
	'''
	copy & deepcopy 테스트
	'''
	import copy

	class Bus:
		def __init__( self , passeners ):
			self.passeners = [] if passeners is None else list(passeners)

		def __str__( self ):
			return '{}'.format(self.passeners)

		def add(self , data):
			self.passeners.append(data)

		def remove( self , data):
			self.passeners.remove(data)


	b1 = Bus(['xferlog' , 'kknda' , 'kcwda' , 'ddd'])
	b2 = copy.copy(b1)
	b3 = copy.deepcopy(b1)
	print('b1 : {} - b2:{} - b3:{}'.format(b1 , b2 , b3))
	print('b1 : {} - b2 : {} - b3:{}'.format(id(b1) , id(b2) , id(b3)))
	print('-'*20)
	b2.remove('kcwda')
	print('b1 : {} - b2:{} - b3:{}'.format(b1 , b2 , b3))
	print('b1 : {} - b2 : {} - b3:{}'.format(id(b1) , id(b2) , id(b3)))

			



import heapq
class PriorityQueue:
	"""
	우선순위 queu 구현
	"""
	def __init__( self ):
		self._queue = []
		self._index = 0


	def push( self , priority , item):
		heapq.heappush( self._queue , (-priority , self._index, item))
		self._index += 1

	def pop(self):
		return heapq.heappop(self._queue)[-1]








def heapq_tst2():
	pq = PriorityQueue()
	pq.push('xferlog',10)
	pq.push('cwkim' , 2)
	pq.push('ejkim',-1)

	print('1 : {}'.format(pq.pop()))
	print('2 : {}'.format(pq.pop()))
	print('3 : {}'.format(pq.pop()))








def heapq_tst():
	"""
	 - 컬렉션 내부에서 가장 크거나 작은 N개의 아이템을 찾는다.
	 - 찾고자 하는 item의 개수가 상대적으로 작을경우 유용하다
	 - 최소값  , 최대값을 구할경우에는 min() , max() 메소드가 더 유용하다.
	"""
	import heapq

	nums = [1,8,2,23,7,-1,18,23,42,37,2]
	nl = heapq.nlargest(3 , nums)
	print('nl : {}'.format(nl))

	sl = heapq.nsmallest(3 , nums)
	print('sl : {}'.format(sl))


	portfolio = [
		{'name':'IBM','shares':100,'price':91.1},
		{'name':'AAPL','shares':50,'price':543.22},
		{'name':'FB','shares':200,'price':21.09},
		{'name':'HPQ','shares':35,'price':31.75},
		{'name':'YHQQ','shares':45,'price':16.35},
		{'name':'ACME','shares':75,'price':115.65}
	]

	sss = heapq.nlargest(2,portfolio , key = lambda x:x['price'] )
	print('sss : {}'.format(sss))
	smin = min(portfolio , key = lambda x:x['shares'])
	print('smin : {}'.format(smin))



if __name__ == '__main__':
	# heapq_tst()
	# heapq_tst2()
	# copyTst()

	weakrefTst()







