#!python3
#-*- coding:utf-8 -*-



def tst1():
	import time
	from progress.bar import PixelBar

	with PixelBar('Progressing...' , max = 5) as bar:
		for i in range(5):
			time.sleep(0.06)
			bar.next()



if __name__ == '__main__':
	tst1()