#!python3
#-*- coding:utf-8 -*-



"""
패밀리 레스토랑에 가서 ,여려 개의 테이블에 사람을 나누어 앚게 하려고 합니다.이때,
한 사람만 있는 테이블이 없게 그룹을 지어야 합니다.
인원수를 나누는 패턴만 구하면 되며 , 누가 어디어 않는지 등은 고려하지 않아도 괜찮습니다.
예을 들어 6명이라면 , 다음과 같은 4가지가 됩니다.
 - 2 + 2 + 2
 - 2 + 4
 - 3 + 3
 - 6

 한개의 테이블에 앉을수 있는 사람은 최대 10명입니다. 100명이 하나 이상의 테이블에 나누어 앉는 패턴을 
 구하세요.
"""

min_value = 2
max_value = 10
totalCount = 100
tableCount = 1



def findDivideNum():
	global min_value
	global max_value
	global totalCount

	dValue = min_value
	minValue = -1
	for _ in range(100):
		v = totalCount%min_value
		if (min_value > v) and (min_value + v <= max_value):
			print('{} :{} - {}'.format(dValue , min_value , v))
			if minValue == -1:
				minValue = max_value - (min_value + v)
			else:
				if minValue >  max_value - (min_value + v):
					minValue = max_value - (min_value + v)
					dValue = min_value
				min_value += 1

	print('dvalue : {}'.format(dValue))
	return dValue



def part(table_num ):
	global totalCount
	global tableCount

	if totalCount >= table_num:
		totalCount -= table_num
		if totalCount < table_num:
			table_num += totalCount
		print('[{}] table num : {}'.format(tableCount , table_num))
		tableCount +=1
		part(table_num)
	else:
		return 0



if __name__ == '__main__':
	part(findDivideNum())

