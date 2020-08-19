#!python3
#-*- coding:utf-8 -*-



from operator import itemgetter

SAMPLE_STR = 'xferlogickaodfk'


def str_sort():
	print('{}'.format(SAMPLE_STR))
	sort_sample_str = sorted(SAMPLE_STR)
	print('{}'.format(''.join(sort_sample_str)))
	r_sorted_sample_str = sorted(SAMPLE_STR , reverse = True)
	number = 1
	print('{} : {}'.format(number , r_sorted_sample_str))





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


	def s( tt ):
		return tt[2]

	students = [
        ('홍길동', 3.9, 2016303),
        ('김철수', 3.0, 2016302),
        ('최자영', 4.3, 2016301),
	]

	print('*'*50)
	print('students : {}'.format(students))
	# case 1 : lambda
	s_students = sorted(students , key = lambda s:s[2] )
	# case 2 : function
	s_students = sorted(students , key = s )
	print('s_students : {}'.format(s_students))
	


def dict_tst():
	sample_dict = {1:'xferlog' , 2:'a' , 3:'kknda'}
	print('-'*20+'-'*20)
	a_sort_dict = sorted(sample_dict.items() , key = itemgetter(0))
	print(a_sort_dict)

	print('-'*20+'-'*20)
	d_sort_dict = sorted(sample_dict.items() , key = itemgetter(0) , reverse = True)
	print(d_sort_dict)



def reverse( word ):
	return word[::-1]




if __name__ == '__main__':
	# dict_tst()


	 str_sort()

	# list_tst()

	# print('\"xferlog\" reverse : {}'.format(reverse('xferlog')))


	# fruits = ['strawberry' , 'fig' , 'apple' , 'cherry' , 'raspberry' , 'banna']

	# print('before : {}'.format(fruits))
	# rev = sorted(fruits , key = reverse)
	# print('after : {}'.format(rev))









