#!python3
#-*- coding:utf-8 -*-



# logging 기능
########################################################################

def my_log( func ):
	def wrapper( *args , **kargs ):
		import logging
		logging.basicConfig(level = logging.INFO , format = '%(asctime)s - %(levelname)s - %(message)s' )
		logging.info('[wrapper] args = {} , kargs = {}'.format(args , kargs))
		return func(*args , **kargs)
	return wrapper



def my_timer( func ):
	def wrapper( *args , **kargs ):
		import timeit
		import logging
		logging.basicConfig(level = logging.INFO , format = '%(asctime)s - %(levelname)s - %(message)s' )

		start = timeit.default_timer()
		result = func(*args , **kargs )
		logging.info('{} - {}'.format(func.__name__ , int(timeit.default_timer() - start)))
		return result
	return wrapper



@my_timer
@my_log
def sum(x,y,z):
	return x+y+z





########################################################################


def outer_function( msg ):
	def inner_function():
		print(msg)
	return inner_function




def tst1():
	hi_func = outer_function('hi')
	bye_func = outer_function('bye')
	hi_func()
	bye_func()



if __name__ == '__main__':
	x = sum(1,2,3)
	print('x : {}'.format(x))






