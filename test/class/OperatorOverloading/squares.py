#!python3
#-*- coding:utf-8 -*-


def test1():
	class Squares:
		def __init__( self , start , end ):
			self.start = start-1
			self.end = end

		def __iter__( self ):
			return self


		def __next__( self ):
			if self.start == self.end:
				raise StopIteration
			self.start +=1
			return self.start ** 2


	s = Squares(2,10)
	for ss in s:
		print('ss : {}'.format(ss))


def test2():

	class Test:
		def __init__( self , _data = None , _start = 0 , _end = 0):
			self.data = [] if _data == None else _data
			self.start = _start
			self.end = len(self.data) if _end == 0 else _end

		def __iter__( self ):
			return self

		def __next__( self ):
			if self.start == self.end or self.start == len(self.data):
				raise StopIteration

			ret = self.data[self.start]
			self.start += 1
			return ret

		def add(self , _data ):
			import copy
			self.data.append(_data)
			self.start = 0
			self.end = len(self.data)


	t = Test(['xferlog' , 'kknda'])
	for s in t:
		print('s : {}'.format(s))
	print('-'*20)

	t.add('khlee')
	for s in t:print('s : {}'.format(s))



def test3():
	'''
	__iter__ , __getitem__ , __contains__
	'''
	class Test:
		def __init__( self , _data = None , _start = 0 , _end = 0):
			self.data = [] if _data == None else _data
			self.start = _start
			self.end = len(_data) if _end == 0 else _end


		def __iter__( self ):
			for d in self.data:
				yield d

		def __getitem__( self , index ):
			return self.data[index]

		def __contains__( self , x ):
			print('x : {}'.format(x))
			return x in self.data

				

	t = Test(['xferlog' , 'kknda' , 'kcwda'])
	for s in t:
		print('s : {}'.format(s))

	print('-'*20)
	print('t : {}'.format(t[1]))
	print('-'*20)
	for s in t:
		print('s : {}'.format(s))

	print('-'*20)
	print('aaa' in t)






if __name__ == '__main__':
	# test1()
	# test2()

	test3()







