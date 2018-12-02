#!python3
#-*- coding:utf-8 -*-


import os , sys
import traceback
import multiprocessing


class MyProcess( multiprocessing.Process ):
	def __init__( self , pipein ):
		super( MyProcess , self ).__init__()
		self.pipein = pipein



	def run( self ):
		try:
			raise Exception('This broke stuff')
		except:
			except_type , except_class , tb = sys.exc_info()

		self.pipein = os.fdopen( self.pipein , 'w')
		self.pipein.write(str(except_type))
		self.pipein.close()




def main():
	pipeout , pipein = os.pipe()
	mp = MyProcess( pipein )
	mp.start()
	mp.join()

	os.close( pipein )
	pipeout = os.fdopen( pipeout )

	pipeContent = pipeout.read()
	print('exception : {}'.format(pipeContent))



if __name__ == '__main__':
	main()