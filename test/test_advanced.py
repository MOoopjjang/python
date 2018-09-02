#!python3
#-*- coding:utf-8 -*-



import collections
from collections import deque



# Magic Method Test Class
###############################################################
class tmp:
	def __init__( self  , _n = 0):
		print('{}.__init__'.format(__file__))
		self.n = _n


	def __str__( self ):
		return str(self.n)

	def __iadd__( self , target):
		print('type : {}'.format(target.n))
		self.n += target.n
		print('n : {}'.format(self.n))
		return self


###############################################################



class multitmp:
	def __init__( self ):
		self._threadings_ = []
		self._dq_ = deque(range(1000) , maxlen = 1000)
		self._ll_ = []

		


	def __set_func__( self , _thread_idx ):
		print('--__set_func__ tid : {} --'.format(_thread_idx))
		for i in range(_thread_idx*100 , _thread_idx*100 + 100):
			self._dq_[i]=str(i)
			print('set -- {}:{}:{}'.format(_thread_idx , i , self._dq_[i]))

	def __get_func__( self , _thread_idx ):
		print('--__get_func__ tid : {} --'.format(_thread_idx))
		for i in range(_thread_idx*100 , _thread_idx*100 + 100):
			print('get -- {}:{}:{}'.format(_thread_idx ,i , self._dq_[i]))




	def run( self ):
		import threading
		import random

		for idx in range(10):
			t = threading.Thread(target = self.__set_func__ , args = ( idx ,))
			t1 = threading.Thread(target = self.__get_func__ , args = ( idx ,))
				

			self._threadings_.append(t)
			self._threadings_.append(t1)
			t1.daemon = True
			t.daemon = True
			t.start()
			t1.start()


		for t in self._threadings_:
			t.join()




def exam_ttt():
	m = multitmp()
	m.run()



def exam_2to23():
	from collections import deque

	dq = deque(range(10 ), maxlen = 10)
	print('1>>  {}'.format(dq))

	dq.rotate(3)
	print('2>>  {}'.format(dq))

	dq.rotate(-4)
	print('3>>  {}'.format(dq))

	dq.appendleft(-1)
	print('4>>  {}'.format(dq))

	dq.extend([11,22,33])
	print('5>>  {}'.format(dq))

	dq.extendleft([-10,-20,-30])
	print('6>>  {}'.format(dq))




def exam_2to21():
	import array
	numbers = array.array('h' , [-2 , -1 , 0 , 1 , 2])
	memv = memoryview(numbers)
	print('exam_2to21:1 >>{}'.format(len(memv)))
	print('exam_2to21:2 >>{}'.format(memv[0]))
	memv_oct = memv.cast('B')
	print('exam_2to21:3 >>{}'.format(memv_oct[0]))



def exam_2to20():
	from array import array
	from random import random
	floats = array('d' , (random() for i in range(10**7)))
	print('1>>{}'.format(floats[-1]))

	fp = open('floats.bin' , 'wb')
	floats.tofile(fp)
	fp.close()

	floats2 = array('d')
	fp = open('floats.bin' , 'rb')
	floats2.fromfile(fp , 10**7)
	fp.close()
	print('2>>{}'.format(floats2[-1]))
	if floats2 == floats:
		print('True!!!')



def exam_tmp1():
	t1 = tmp(0)
	print('t1>>{}'.format(t1))

	t2 = tmp(1)
	print('t2>>{}'.format(t2))

	t3  = tmp(9)
	print('t3 b>>{}:{}'.format(id(t3) , t3))
	t3 += t2
	print('t3 a>>{}:{}'.format(id(t3) , t3))




def exam_2to12():
	board = [['_']*3 for i in range(3)]
	print('board>>{}'.format(board))
	board[1][2] = 'x'
	print('board>>{}'.format(board))

	weird_board = [['_']*3]*3
	print('weird_board>>{}'.format(weird_board))
	weird_board[1][2] = 'O'
	print('weird_board>>{}'.format(weird_board))


def exam_2tot1():
	l = list(range(10))
	print('l>>{}'.format(l))
	l[2:5] = [20 , 30]
	print('l>>{}'.format(l))
	del l[2:4]
	print('l>>{}'.format(l))
	l[2:4] = [100] 
	print('l>>{}'.format(l))

	l *= 5
	print('l>>{}'.format(l))





def exam_2to9():
	st = ('xferlog',)
	print('st>>{}'.format(st))
	print('st.type>>{}'.format(type(st)))
	City = collections.namedtuple('City' , 'name country population coordinates')
	tokyo = City('Tokyo' , 'JP' , 36.933 , (35.483939 , 139.8392))
	# print('{}'.format(tokyo))
	# print('{}'.format(tokyo.coordinates))
	# print('{}'.format(tokyo[1]))
	print('City>> {}'.format(City._fields))

	LatLong = collections.namedtuple('LatLong' , 'lat long')
	print('LatLong>> {}'.format(LatLong._fields))
	delhi_data = ('Delhi NCR' , 'IN' , 21.935 , LatLong(28.94984 , 77.7848))
	print('delhi_data>> {}'.format(delhi_data))
	delhi = City._make(delhi_data)
	print('delhi>> {}'.format(delhi._asdict()))




def main():
	# exam_2to9()
	# exam_2tot1()
	# exam_2to12()
	# exam_2to20()
	# exam_2to21()
	# exam_2to23()

	# exam_tmp1()
	exam_ttt()


	

if __name__ == '__main__':
	main()