#!python3
#-*- coding:utf-8 -*-



def logger( msg ):
	def logger_msg():
		print(msg)
	return logger_msg


def outer_func( ):
	msg = 'hi'
	def inner_func():
		print(msg)
	return inner_func




if __name__ == '__main__':

	# f = logger('hello')
	# print('f : {}'.format(f))
	# f()
	# del logger
	# try:
	# 	print('{}'.format(logger))
	# except:
	# 	print('logger not found!!')
	# f()


	fu = outer_func()

	print ('fu : {}'.format(fu))
	print('-'*10)
	print ('dir fu : {}'.format(dir(fu)))
	print('-'*10)
	print ('type fu.__closure__ : {}'.format(type(fu.__closure__)))
	print('-'*10)
	print ('fu.__closure__ : {}'.format(fu.__closure__))
	print('-'*10)
	print ('dir(fu.__closure__[0]) : {}'.format(dir(fu.__closure__[0])))
	print('-'*10)
	print ('fu.__closure__[0].cell_contents : {}'.format(fu.__closure__[0].cell_contents))
	print('-'*10)