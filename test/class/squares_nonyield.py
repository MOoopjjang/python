#!python3
#-*- coding:utf-8 -*-


"""
  다중 스캔..
"""

class SquaresIterator:
	def __init__( self , start , data ):
		self.data = data
		self.start = start

	def __next__( self ):
		if  self.start >= len(self.data):
			raise StopIteration
		else:
			v = self.data[self.start]
			self.start +=1
			return v


class Squares:
	def __init__( self , data ):
		self.data = data
		self.start = 0


    
	def __iter__( self ):
		"""
		generator를 사용하지 않는 multiscan
		"""
		return SquaresIterator( self.start , self.data )

	def __iter__( self ):
		"""
		generator를 사용한 multiscan
		"""
		for i in range(len(self.data)):
			yield self.data[i]



if __name__ == '__main__':
	s = Squares('xferlogkknda')

	it = iter(s)
	print(next(it) , next(it))

	for i in s:
		for j in s:
			print(i+j,end = ' ')




