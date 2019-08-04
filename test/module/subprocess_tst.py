#!python3
#-*- coding:utf-8 -*-


import subprocess
import os


def tst1():
	print('*'*10+'call'+'*'*10)
	subprocess.call(args = ['ls' , '-l'] , shell=False)
	print('*'*10+'run'+'*'*10)
	subprocess.run(args = ['ls -al'] , shell = True)


def tst2():
	subprocess.run(args = ['python test.py'] , shell = True)

	subprocess.run(['open' , '/Users/mooopjjang/Downloads/PDPopDownload/rpoing.mp4'])


def tst3():
	with open('output.txt' , 'w') as fw:
		output = subprocess.check_output(['python' , 'test.py'] , encoding='utf-8')
		fw.write(output)




if __name__ == '__main__':
	# tst1()
	# tst2()
	tst3()