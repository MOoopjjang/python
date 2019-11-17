#!python3
#-*- coding:utf-8 -*-





def search(_pattern , lines , history = 5 ):
	from collections import deque

	previous_lines = deque(maxlen = history )
	for line in lines:
		if _pattern in line:
			yield line , previous_lines
		previous_lines.append(line)





def tst_2():
	with open('tmp.txt') as f:
		for line , plines in search('python' , f , 5):
			for pline in plines:
				print(pline , end='')
			print(line , end='')
			print('-'*20)




def tst_1():
	sample = 'xferlog'
	_,a,*b = sample
	print('a:{} , b:{}'.format(a,b))

	records = [
		('cwkim' , 43 , 'seni'),
		('khlee' , 40 , 'team' , 11),
		('kang' , 32 , 'junior')
	]


	for name , *infos in records:
		print('name : {} - {}'.format(name , infos))
		s = len(infos)
		print('len : {}'.format(s))




if __name__ == '__main__':
	# tst_1()

	tst_2()




