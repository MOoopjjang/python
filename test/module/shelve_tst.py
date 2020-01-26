#!python3
#-*- coding:utf-8 -*-


'''
 - binary 형태로 데이타 저장
 - dict형태와 유사한 데이타 저장방식 구조
   
'''

import shelve




def usage():
	# write
	with shelve.open('mydata') as shfile:
		aninmals = ['cat' , 'dog' , 'monkey']
		shfile['anis'] = aninmals


	with shelve.open('mydata') as shfile:
		print(type(shfile))
		print('anis : {}'.format(shfile['anis']))

		print(list(shfile.keys()))
		print(list(shfile.values()))




if __name__ == '__main__':
	usage()