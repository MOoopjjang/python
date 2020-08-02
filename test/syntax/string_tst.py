#!python3
#-*- coding:utf-8 -*-




"""
string 테스트
"""



SAMPLE_1 = 'xferlog kknda iablc iadifladkfalkflkak123 :'




def tst1():
	if SAMPLE_1.startswith('xferlog'):print('e')
	else:print('ne')

	print('-'*30)
	if SAMPLE_1.endswith('123 :'):
		print('e')
	else:
		print('ne')

	print('-'*30)
	print('upper : {}'.format(SAMPLE_1.upper()))
	print('lower : {}'.format(SAMPLE_1.lower()))
	print('-'*30)
	r = SAMPLE_1.replace(' ','')
	print('r : {}'.format(r))
	print('-'*30)
	print('{}'.format(SAMPLE_1[3:10]))
	print('{}'.format(SAMPLE_1[3:10:2]))
	print('-'*30)
	LIST = list(SAMPLE_1)
	print('list : {}'.format(LIST))
	print('-'*30)
	t = tuple(SAMPLE_1)
	print('tuple : {}'.format(t))
	print('-'*30)
	print('find "iablc" : {}'.format(SAMPLE_1.find('iablc')))
	print('-'*30)
	f = list(filter(lambda x:x != ' ',SAMPLE_1))
	print('f : {}'.format(f))




if __name__ == '__main__':
	tst1()
