#!python3
#-*- coding:utf-8 -*-

SAMPLE_DATA1 = '1,2,3'
SAMPLE_DATA2 = '3,4,5'

def tst2():
	s1 = set([1,2])

	s1.add(7)
	print('add 7 : {}'.format(s1))

	s1.update([3,4,5])
	print('s1 : {}'.format(s1))

	s1.remove(4)
	print('s1 : {}'.format(s1))


def tst1():
	s1 = set(SAMPLE_DATA1.split(','))
	s2 = set(SAMPLE_DATA2.split(','))
	print('s1 : {} -- s2 : {}'.format(s1 , s2))
	print('-'*20)
	sv1 = s1 | s2
	print('합집합 : {}'.format(sv1))
	sv2 = s1 & s2
	print('교집합 : {}'.format(sv2))
	sv3 = s1 - s2
	print('차집합 : {}'.format(sv3))
	sv4 = s1^s2
	l = list(sv4)
	l.sort()
	print('대칭차집합 : {}'.format(set(l)))




if __name__ == '__main__':
	 tst1()
	#tst2()