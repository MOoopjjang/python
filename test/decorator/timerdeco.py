#!python3


import timeit

def Timer(label = '' , trace = True):
	class timer:
		def __init__( self , func ):
			self.func = func

		def __call__( self , *args , **kargs):
			start = timeit.default_timer()
			result = self.func(*args , **kargs)
			if trace:
				print('%s [%s] consume time : %s'%( label ,self.func.__name__ , timeit.default_timer() - start))
			return result
	return timer


@Timer('-->')
def listcomp(X):
	return [ v**2 for v in range(X)]

@Timer('==>' , False)
def mapcomp(X):
	return list(map(lambda xx:xx*2 , range(X)))


if __name__ == '__main__':
	l = listcomp(1000000)

	ll = mapcomp(1000000)