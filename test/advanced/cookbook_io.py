#!python3
#-*- coding:utf-8 -*-




def tst_8():
	'''
	디렉토리 내의 파일리스트 구하기
	'''
	import os

	path = '/Users/gimcheol-u/Documents/work/git/python/test/advanced'
	# path = '/Users/gimcheol-u/Documents/work/git/python/test/advanced/tmp.txt'

	if os.path.isdir(path):
		for f in os.listdir(path):
			print('{}'.format(f))
	else:
		print('{}'.format(os.path.splitext(path)))




def tst_7():
	'''
	기본파일이름 , 디렉토리 이름 , 절대 경로등
	'''

	import os

	path = '/Users/gimcheol-u/Documents/work/git/python/test/advanced/tmp.txt'

	print('file name : {}'.format(os.path.basename(path)))
	print('dir name : {}'.format(os.path.dirname(path)))

	print('파일경로 합치기 : {}'.format(os.path.join('/Users/gimcheol-u/Documents/work/git/python/test/advanced','tmp.txt')))
	print('파일확장자분리 : {}'.format(os.path.splitext(path)))



def tst_6():
	'''
	바이너리 파일을 수정 가능한 바이트 배열에 매핑하고 , 내용에 접근하거나 수정하고 싶다.
	'''

	import os
	import mmap

	SSIZE = 1000000

	def memory_map( filename , access = mmap.ACCESS_WRITE ):
		size = os.path.getsize( filename )
		print('org size : {}'.format(size))
		fd = os.open( filename , os.O_RDWR )
		return mmap.mmap( fd , size , access = access )


	with open('data' , 'wb') as f:
		f.seek(SSIZE-1)
		f.write(b'\x00')




	buf = memory_map( 'data')
	print('len : {}'.format(len(buf)))
	print('{}'.format(buf[0:10]))

	#slice 재할당
	buf[0:11] = b'hello world'
	buf.close()


	with open('data' , 'rb') as fr:
		print(fr.read(11))


	with memory_map('data') as m:
		print(len(m))
		print(m[0:len(m)-1])



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
	# tst_5()
	# tst_6()
	# tst_7()
	tst_8()



