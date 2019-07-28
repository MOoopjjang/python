#!python3
#-*- coding:utf-8 -*-



from operator import itemgetter


def str_sort():
	sample1 = 'akcmakam12mcldkad9rmckadjf'
	print('-------- sorted 3rd index ------------')
	s_str1 = ''.join(sorted(sample1))
	print(s_str1)
	print('-------- sorted 3rd index ------------')
	s_str1 = ''.join(sorted(sample1 , reverse = True))
	print(s_str1)


def list_tst():
	category = [
	[200130 , 32000 , 'Google' , 5.96 , 71325],
	[200130 , 32000 , 'Netflix' , 5.96 , 30000],
	[200230 , 17400 , 'FaceBook' , 29.85 , 25751012],
	[206640 , 18750 , 'Amazon' , 6.53 , 214676]
	]


	print('-------- sorted 3rd index ------------')
	category.sort(key = itemgetter(2))
	print(category)
	

	print('-------- sorted 3rd index reverse ------------')
	category.sort(key = itemgetter(2) , reverse = True)
	print(category)
	

	print('-------- sorted multiple index( 3 , 4) index reverse ------------')
	category.sort(key = itemgetter(3 , 4))
	print(category)
	


def dict_tst():
	sample_dict = {1:'xferlog' , 2:'a' , 3:'kknda'}
	print('-'*20+'-'*20)
	a_sort_dict = sorted(sample_dict.items() , key = itemgetter(0))
	print(a_sort_dict)

	print('-'*20+'-'*20)
	d_sort_dict = sorted(sample_dict.items() , key = itemgetter(0) , reverse = True)
	print(d_sort_dict)




if __name__ == '__main__':
	# dict_tst()

	list_tst()

	# str_sort()
