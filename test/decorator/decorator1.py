#!python
#-*- coding:utf-8 -*-



class tracer:
	def __init__( self , func ):
		self.count = 0
		self.func = func

	def __call__( self , *args , **kargs ):
		self.count +=1
		print('%s - %s'%(self.count , self.func.__name__))
		print('%s - %s'%(args , kargs))
		return self.func(*args , **kargs)


def ftracer(func):
	def Wrapper(*args):
		Wrapper.call_count +=1
		print('%s - %s'%(Wrapper.call_count , func.__name__))
		return func(*args)

	Wrapper.call_count = 0
	return Wrapper


# @ftracer
@tracer
def spam(a , b ,c):
	return a+b+c



if __name__ == '__main__':

	s = spam(1,2,3)
	print('s : %s'%s)

	s = spam(a=4,b=5,c=6)
	print('s : %s'%s)