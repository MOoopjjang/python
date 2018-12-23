#!python3
#-*- coding:utf-8 -*-


class Squares:
	def __init__( self , start , stop ):
		self.value = start-1
		self.stop = stop

	def __iter__( self ):
		return self

	def __next__( self ):
		if self.value == self.stop:
			raise StopIteration
		self.value +=1
		return self.value ** 2



def gsquares( start , stop ):
	for i in range( start , stop + 1):
		yield i ** 2




def main():
	# for i in Squares(1 , 5):
	# 	print(i,end=' ')


	# x = Squares(1,5)
	# it = iter(x)
	# print('{}'.format(next(it)))
	# print('{}'.format(next(it)))


	# x = Squares(1,5)
	# print('{}'.format([i for i in x ]))
	# print('{}'.format([i for i in x ]))


	for i in gsquares(1 , 5):
		print(i , end = ' ')

	for i in (x ** 2 for x in range(1,6)):
		print(i , end = ' ')



if __name__ == '__main__':
	main()