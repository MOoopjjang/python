#!python3




from processor import Processor



class Uppercase( Processor ):
	def __init__( self , _reader , _writer ):
		Processor.__init__( self , _reader , _writer )

	def converter( self , data ):
		return data.upper()



if __name__ == '__main__':
	import sys
	obj = Uppercase(open('contains.py') , sys.stdout)
	obj.process()
