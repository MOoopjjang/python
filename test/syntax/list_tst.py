#!python3
#-*- coding:utf-8 -*-



import os , sys
import copy

def main():
	spam = ['xferlog' , 'kknda' , 'bhkim' , 'ejkim']
	print(spam)
	del spam[2]
	print(spam)

	if 'ejkim'  not in spam:
		print('exist!')


	a , b , c = spam
	print(a+':'+b+':'+c)	

	print(spam.index('kknda'))

	spam.insert(2,'ccccc')
	print(spam)

	sssss = 'xferlog hi how are you?'
	bhss = sssss.replace('kcwda' , 'bhkim')
	print(sssss)
	# ssl = list(sssss)
	# ssl.replace('kcwda' , 'bhkim')
	

	print(bhss)

	list_ss = list(sssss)
	list_ss[:len('xferlog')] = 'bhkim'
	convert_str = ''.join(list_ss)
	print(convert_str)

	t_l_s = tuple(list_ss)
	print(t_l_s)
	l_t_s = list(t_l_s[0:len('bhkim')])
	print(l_t_s)

	tt = ('xferlog',)
	print(type(tt))

	bl = ['kknda' , 'bhkim']
	cl = copy.deepcopy(bl)
	cl[0]='kkk'
	print(bl)
	print(cl)




if __name__ == '__main__':
	main()