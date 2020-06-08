#!python3
#-*- coding:utf-8 -*-


import random


'''
 1. 덧셈 , 뺄셈 , 곱셈 문제를 임의로 만들어 보여 줍니다.
 2. 사용자가 답을 입력
 3. 정답인지 ,  오답인지 알려줌
 4. 계산하여 점수를 매김
 5. 이과정을 5번 반복
 6. 전체 정답수를 알려준다.
'''

OPERATION = ['+' , '-' , '*' , '/']
HIT = {}

def random_value():
	return random.randint(1,100)


def get_operation():
	return OPERATION[random.randint(0,3)]


def hit_inf( idx , result ):
	HIT[idx] = result



if __name__ == '__main__':
	for idx in range(0,5):
		l = random_value()
		r = random_value()

		if l < r:
			tmp = l
			l = r
			r = tmp

		o = get_operation()
		v = 0
		if o is '+':v = l+r
		elif o is '-':v = l-r
		elif o is '*':v = l*r
		else:
			v = int(l/r)

		input_num = int(input('{} {} {} ?'.format(l,o,r)))
		if input_num == v:
			hit_inf(idx , v)
			print(' 정답입니다. ')
		else:
			print('오답입니다.')


	print('*'*20)
	for k,v in HIT.items():
		print('{} => {}'.format(k,v))
	print('*'*20)




