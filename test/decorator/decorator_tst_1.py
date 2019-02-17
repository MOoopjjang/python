#!python3



def decorator( F ):
	def wrapper(*args):
		wrapper.count += 1
		print('wrapper : %s'%wrapper.count)
		return F(*args)

	
	wrapper.count = 0
	print('sssssss : %s'%wrapper.count)
	return wrapper


@decorator
def func( x , y , z):
	return x+y+z



class C:
	@decorator
	def method(self , x,y,z):
		return x+y+z




if __name__ == '__main__':
	# s = decorator(func)(10 , 11 , 12)
	s = func(10 , 11 , 12)
	print('s : %s'%s)

	s = func(10 , 11 , 12)
	print('s : %s'%s)

	s = func(10 , 11 , 12)
	print('s : %s'%s)


	c = C()
	ss = c.method(1,2,3)
	print('ss : %s'%ss)


