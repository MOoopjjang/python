#!python3
#-*- coding:utf-8 -*-




"""
string 테스트
"""



SAMPLE_1 = 'xferlog kknda iablc iadifladkfalkflkak123'


def tst_1():
	splits = SAMPLE_1.split(' ')
	print(splits)


	print('-'*40)
	start_i = [ s for s in SAMPLE_1.split(' ') if s.startswith('i') ]
	print(start_i)

	print('-'*40)
	if 'ab' in SAMPLE_1:
		print('\"ab\" contains')


	print('-'*20+'upper'+'-'*20)
	print(SAMPLE_1.upper())

	print('-'*20+' a b i upper'+'-'*20)

	output = ''
	for s in SAMPLE_1:
		output += s.upper() if s == 'i' or s == 'a' or s == 'b' else s
		
	print(output)

	print('-'*20+'replace'+'-'*20)
	rep_sam = SAMPLE_1.replace('kknda' , 'bhkim')
	print(rep_sam)

	print('-'*20+'join'+'-'*20)
	l = ['xferlog' , 'kknda' , 'ccccc' , 'dddd']
	jstr = '<<>>'.join(l)
	print(jstr)






if __name__ == '__main__':
	tst_1()
