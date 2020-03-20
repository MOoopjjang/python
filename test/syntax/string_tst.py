#!python3
#-*- coding:utf-8 -*-




"""
string 테스트
"""



SAMPLE_1 = 'xferlog kknda iablc iadifladkfalkflkak123 :'




def tst1():
	strip_str = SAMPLE_1.strip()
	print('strip_str : {}'.format(strip_str))
	print(' ":" remove :{}'.format(SAMPLE_1.strip(':')))

	#replace test
	print('":" --> "=" : {}'.format(SAMPLE_1.replace(':' , '=')))

	# SAMPLE_1[3] = 'k'

	l = list(SAMPLE_1)
	l[3] = 'k'
	print(''.join(l))

	# split 테스트
	print('split test : {}'.format(SAMPLE_1.split(' ')))


	x = SAMPLE_1.find('kknda')
	print('find "kknda" : {}'.format(x))


if __name__ == '__main__':
	tst1()
