#!python3
#-*- coding:utf-8 -*-






def fact(n , limit , mul):
	print('{} - {} - {}'.format(n , limit , mul))
	if n > limit:
		return mul
	else:
		return fact(n+1 , limit , mul * n)



def fact1(n):
	return n*fact1(n-1)



def gcd(n,n1):
	"""
	최대 공약수 구하기
	"""

	m = min(n,n1)
	print('m - {}'.format(m))
	cur = m
	while m > 1:
		if n%m == 0 and n1%m == 0:
			cur = m
		m -=1

	print('cur : {}'.format(cur))



def func(o , n):
	import os

	print('--- pid :{} --- start'.format(os.getpid()))

	for i in o:
		if i == n:
			print('--- pid :{} --- search : {}'.format(os.getpid() , i))
			break


	print('--- pid :{} --- end'.format(os.getpid()))




def binary_search_tmp(org , n):
	import concurrent.futures
	from concurrent.futures import ThreadPoolExecutor

	with ThreadPoolExecutor(max_workers = 2) as executor:
		d = int(len(org)/2)
		start = 1
		end = 0
		futures = []
		for i in range(0,2):
			start = i*d
			end = start+d
			if end >= len(org):end = len(org)-1
			futures.append(executor.submit(func , org[start:end] , n ))
			for future in concurrent.futures.as_completed( futures):
				print('{}'.format(future.result()))




def searching(org , n):
	size = len(org)
	if size >=4: 
		harf = int(len(org)/2)
		if(org[harf] > n):
			return searching(org[:harf] , n)
		else:
			return searching(org[harf:] , n)
	else:
		for v in org:
			if v == n:
				return 'find'
		return 'not find'


def binary_search( org , n):

	org.sort()
	print('sorg : {}'.format(org))
	return searching( org , n )





if __name__ == '__main__':
	# result = fact(1 , 10 , 1)
	# print('result : {}'.format(result))


	# print('{}'.format(fact1(5)))


	# gcd(22,11)


	result = binary_search([1,2,3,12,839,898,8,0,23,11,90] , 111)
	print('result : {}'.format(result))





