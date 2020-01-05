#!python3
#-*- coding:utf-8 -*-


def tst_6():
	'''
	gzip ,gzip 압축된 파일읽기 , 압축하기
	'''
	import gzip , bz2

	# 압축하기
	with open('')


def tst_5():
	'''
	존재한지 않는 파일에 write ( x mode 사용 )
	'''
	with open('sample_3.txt' , 'x') as fw:
		fw.write('hellow\n')


def tst_4():
	with open('sample_1.txt' , 'rt') as f:
		print('hello world!',file=f)


def tst_3():
	row = ('ACME' , 50 , 91.5)
	print(*row , sep = ',')


def tst_2():
	for i in range(5):
		print(i , end='')


def tst_1():
	with open('sample_1.txt' , 'rt' , encoding='utf-8') as fr:
		for line in fr:
			print(line , end='')


if __name__ == '__main__':
	# tst_1()
	# tst_2()
	# tst_3()
	# tst_4()

	tst_5()