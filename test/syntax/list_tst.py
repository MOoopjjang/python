#!python3
#-*- coding:utf-8 -*-



import os , sys

def main():
	print('{}'.format([1,2,3]*3))

    # 다중할당기법
	a = [1,2,3]
	one , two , three = a
	print('{} , {} , {}'.format(one , two , three))

	# method -- index()
	ar1 = ['xferlog' , 'kknda' , 'abc']
	print('index -- {}'.format(ar1.index('kknda')))
	# print('index -- {}'.format(ar1.index(1)))

	#        -- insert
	ar1.insert(2,'kcwda')
	print('ar1 : {}'.format(ar1))

	#        -- remove
	ar1.remove('kcwda')
	print('remove - ar1 : {}'.format(ar1))


	t = tuple([1,2,3])
	print('t : {}'.format(t))

	l = list((3,4,5))
	print('l: {}'.format(l))


if __name__ == '__main__':
	main()