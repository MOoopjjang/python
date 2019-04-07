#!python3
#-*- coding:utf-8 -*-


class Person:
	def __init__( self):
		self._list = []
		self._index = 0


	def __setitem__( self , index , v ):
		self._list.insert(index , v)

	# def __getitem__( self , index ):
	# 	return self._list[index]

	def __iter__( self ):
		return self

	def __next__( self ):
		size = len(self._list)
		if self._index == size:
			raise StopIteration
		else:
			r = self._list[self._index]
			self._index += 1
			return r

	def __str__( self ):
		return '[%s] %s'%(self.__class__.__name__ , self._list)


class Square:
	def __init__( self , start , end ):
		self._start = start
		self._end = end

	def __getitem__( self , index):
		return self._data[index]

	def __iter__( self ):
		return self

	def __next__( self ): 
		if self._start == self._end:
			raise StopIteration
		else:
			r = self._start ** 2
			self._start += 1
			return r


if __name__ == '__main__':
	# p = Person()
	# p[0] = 'xferlog'
	# p[1] = 'kknda'
	# print(p)

	# for pp in p:
	# 	print(pp)


	print( 36 in Square( 1 , 10))	
	print(':'.join(map(str , Square(1,10))))

	print('-'*20)
	X = Square(1,5)
	print(tuple(X) , tuple(X))
	print('-'*20)
	tlist = list(Square(1,5))
	print(tuple(tlist) , tuple(tlist))











