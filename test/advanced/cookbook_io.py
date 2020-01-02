#!python3
#-*- coding:utf-8 -*-


def tst_1():
	with open('sample_1.txt' , 'rt' , encoding='utf-8') as fr:
		for line in fr:
			print(line , end='')


def tst_2():
	for i in range(5):
		print(i , end='')


def tst_3():
	row = ('ACME' , 50 , 91.5)
	print(*row , sep = ',')


if __name__ == '__main__':
	# tst_1()
	# tst_2()

	tst_3()