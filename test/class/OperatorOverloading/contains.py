#!python3
#-*- coding:utf-8 -*-


class Iters:
	def __init__( self , data ):
		print('__init__ called')
		self.data = data


	def __getitem__( self , i ):
		print('getitem [%s] :'%i , end = ' ')
		return self.data[i]


	# generator version
	# def __iter__( self ):
	# 	print('iter=> ',end = ' ')
	# 	for x in self.data:
	# 		yield x


	# normal version
	def __iter__( self ):
		print('iter=> ',end = ' ')
		self.i = 0
		return self


	def __next__( self ):
		print('next : ' , end= ' ')
		if self.i >= len(self.data):raise StopIteration
		item = self.data[self.i]
		self.i +=1
		return item


	def __contains__( self , x ):
		print('contains : ' , end = ' ')
		return x in self.data



if __name__ == '__main__':
	X = Iters([1,2,3,4,5,6])
	print('-'*10)
	print(3 in X)
	print('-'*10)
	for i in X:print(i , end = '|')
	print('-'*10)
	print()
	print('-'*10)
	print([i ** 2 for i in X])
	print( list(map(bin , X)))

	I = iter(X)
	while True:
		try:
			print(next(I) , end = ' @ ')
		except StopIteration:
			break





















