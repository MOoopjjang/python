#!python3
#-*- coding:utf-8 -*-


from abc import ABCMeta , abstractmethod



class Super( metaclass = ABCMeta ):
	def delegate( self ):
		self.action()

	@abstractmethod
	def action( self ):
		pass



class Child( Super ):
	def action( self ):
		print(' action ')



if __name__ == '__main__':
	# s = Super()
	# s.action()


	c = Child()
	c.action()
