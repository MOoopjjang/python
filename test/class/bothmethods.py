#!python


class trace:
	def __init__( self , func ):
		self.call = 0
		self.func = func

	def __call__( self , *args ):
		self.call +=1
		print('%s and %s'%(self.call , self.func.__name__))
		return self.func(*args)



def tracer(func):
	def oncall(*args):
		oncall.calls +=1
		print('%s -- %s'%(oncall.calls , func.__name__))
		return func(*args)

	oncall.calls = 0
	return oncall


class C:
	@tracer
	def sam(self , a,b,c):
		return a+b+c


@trace
def sspm(a,b,c):
	return a+b+c

class Method:
	def imeth( self , x ):
		print([self , x ])

	@staticmethod
	def smeth( x ):
		print([x])

	@classmethod
	def cmeth(cls , x):
		print([cls , x])

	# smeth = staticmethod(smeth)
	# cmeth = classmethod(cmeth)



class Spam:
	numm = 0
	def __init__( self ):
		self.count()
	def count( cls ):
		cls.numm +=1
	count = classmethod(count)


class Sub( Spam ):
	numm = 0
	def __init__( self ):
		Spam.__init__( self )


class Other ( Spam ):
	numm = 0









if __name__ == '__main__':
	# Method.smeth(10)
	# Method.cmeth(6)

	# x,a = Sub() , Spam()
	# x.printNumInstance()
	# a.printNumInstance()

	# z = Other()
	# z.printNumInstance()



	# x1,x2 = Sub() , Sub()
	# print(' x1 : %d , x2 : %d'%(x1.numm , x2.numm))

	# print(sspm(1,2,3))
	# print(sspm(10,20,30))


	c = C()
	c.sam(1,2,3)
	c.sam(10,20,30)









