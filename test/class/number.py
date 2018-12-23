#!python3
#-*- coding:utf-8 -*-


class Number:
	def __init__( self , start ):
		self.data = start

	def __sub__( self , other):
		return Number( self.data - other )

	def __getitem__( self , index ):
		return self.data ** 2



class StepperIndex:
	def __getitem__( self , i):
		return self.data[i]




def main():
	x = Number( 10 )
	y = x-2
	print(' -  y : {}'.format(y.data))
	print('y[2] : {}'.format(y[2])) # __getitem__


	a = StepperIndex()
	a.data = 'kknda'
	for item in a:
		print('item : {}'.format(item))

	s = [ item for item in a]
	print('s : {}'.format(s))

	print('k' in a)

	sl = list(map(str.upper , s))
	print('sl : {}'.format(sl))


if __name__ == '__main__':
	main()





	