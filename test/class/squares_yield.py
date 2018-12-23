#!python3
#-*- coding:utf-8 -*-



class squares:
	def __init__( self , start , stop ):
		self.start = start
		self.stop = stop


	def __iter__( self ):
		for value in range(self.start , self.stop + 1):
			yield value ** 2




def main():
	g = squares(1,5)
	for i in g:print(i , end = ' ')



if __name__=='__main__':
	main()