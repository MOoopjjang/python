#!python3
#-*- coding:utf-8 -*-



from operator import itemgetter


def str_sort():
	str_o = 'xferlogickaodfk'

	s_str_o = sorted(str_o)
	print(s_str_o)

	sort_str_r = sorted( str_o , reverse = True )
	print(sort_str_r)



def list_tst():
	category = [
	[200130 , 32000 , 'Google' , 5.96 , 71325],
	[200130 , 32000 , 'Netflix' , 5.96 , 30000],
	[200230 , 17400 , 'FaceBook' , 29.85 , 25751012],
	[206640 , 18750 , 'Amazon' , 6.53 , 214676]
	]


	print('-------- sorted 3rd index ------------')
	# for c in category.sort(key = itemgetter(3)):print(c)
	category.sort(key = itemgetter(3))
	for c in category:print(c)

	print('-------- sorted 3rd index reverse ------------')
	category.sort(key = itemgetter(3) , reverse = True)
	for c in category:print(c)

	print('-------- sorted multiple index( 3 , 4) index reverse ------------')
	category.sort( key = itemgetter( 3 , 4))
	for c in category:print(c)


def dict_tst():
	sample_dict = {'a':10 , 'b':1 , 'f':100 , 'd':8 , 'g':50}

	# print(dir(d))
	key_asc = sorted(sample_dict.items() , key = itemgetter(0))
	key_desc = sorted( sample_dict.items() , key = itemgetter( 0 ) , reverse = True )

	value_asc = sorted( sample_dict.items() , key = itemgetter( 1 ))
	value_desc = sorted( sample_dict.items() ,key = itemgetter( 1 ) , reverse = True)




if __name__ == '__main__':
	# dict_tst()

	# list_tst()

	str_sort()
