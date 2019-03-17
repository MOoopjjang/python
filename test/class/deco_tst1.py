#!python


def tracer( func ):
	def oncall( *args ):
		oncall.calls +=1
		print('%s -- %s'%(oncall.calls , func.__name__))
		return func(*args)
	oncall.calls = 0
	return oncall



class C:
	@tracer
	def sum(self , a , b , c):
		return a + b + c



if __name__ == '__main__':
	c = C()
	# tracer(c.sum)
	c.sum(1 , 2 , 3)
	c.sum(10 , 20 , 30)
