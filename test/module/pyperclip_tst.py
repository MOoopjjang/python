#!python3
#-*- coding:utf-8 -*-


'''
clip board영역에 값을 copy및 paste하는 module
'''

import pyperclip
import sys


def tst_2():
	'''
	clip board 내용 변경
	'''

	buf = pyperclip.paste()
	if buf == None or len(buf) == 0:
		print('empty clip board')
	else:
		print('org : {}'.format(buf))
		output = ''
		tmp = ''
		for c in buf:
			if c != '\n':
				tmp += c
			else:
				output += '[mooop]'+tmp+'\n'
				tmp = ''

		if tmp != '' and len(tmp) > 0:
			output += '[mooop]'+tmp
		print('after : {}'.format(output))
		pyperclip.copy(output)
		print('covert clip board')



def tst_1():
	PASSWORDS = {
		'email':'wpswkd1gkf',
		'redmine':'cwkim123'
	}

	print('len : {}'.format(len(sys.argv)))
	if len(sys.argv) >= 2:
		key = sys.argv[1]
		if key in PASSWORDS:
			pyperclip.copy(PASSWORDS[key])
			print('copy success!!')
		else:
			print('{} not exist!!'.format(key))



def usage():
	pyperclip.copy('hello world')
	print('{}'.format(pyperclip.paste()))


if __name__ == '__main__':
	# usage()

	# tst_1()
	tst_2()




