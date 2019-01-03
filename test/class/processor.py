#!python3


from abc import ABCMeta , abstractmethod


class Processor:
	def __init__( self  , reader , writer ):
		self.reader = reader
		self.writer = writer


	def process( self ):
		while True:
			data = self.reader.readline()
			if not data:break
			data = self.converter( data )
			self.writer.write( data )

	@abstractmethod
	def converter( self , data ):pass
