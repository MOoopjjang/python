#!python3
#-*- coding:utf-8 -*-


"""
custom iterator 객체를 가짐으로써 값을 계속 유지 가능.
  - SkipIterator
"""


class SkipIterator:
	def __init__( self , wrapped ):
		self.wrapped = wrapped
		self.offset = 0

	def __next__( self ):
		if self.offset >= len(self.wrapped):
			raise StopIteration
		else:
			item = self.wrapped[self.offset]
			self.offset +=2
			return item



class SkipObject:
	def __init__( self , wrapped ):
		self.wrapped = wrapped

	def __iter__( self ):
		return SkipIterator( self.wrapped )



if __name__ == '__main__':
	v = 'xferlogkknda'
	x = SkipObject(v)
	it = iter(x)
	print('{} , {} , {}'.format(next(it) , next(it) , next(it)))

	for i in x:
		for j in x:
			print(i+j , end = ' ')