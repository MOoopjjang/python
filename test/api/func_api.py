#!python3
#-*- coding:utf-8 -*-





def mul( _x ):
	return _x **2


def add( _x ):
	return _x + _x


def main():
	num_list = [1,2,3,4,5,6]

	# num_double_list = list(map(mul , num_list))
	# num_double_list2 = list(map(lambda x:x**2 , num_list))
	# print('num_double_list : {}'.format(num_double_list2))


	FUNC_LIST = [mul , add]
	# for func in FUNC_LIST:
	# 	l = list(map(func , num_list))
	# 	print('l : {}'.format(l))


	for i in range(5):
		value = list(map(lambda x:x(i) , FUNC_LIST))
		print('v : {}'.format(value))




if __name__ == '__main__':
	main()