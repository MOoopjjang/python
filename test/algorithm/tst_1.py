#!python3
#-*- coding:utf-8 -*-



def exec_10_2_1( a , b ):
	return 180 - (a+b)


def exec_10_2_2(org):
	tip = 0.1
	tax = 0.07

	tip_org = org * tip
	tax_org = org * tax
	return org + tip_org + tax_org

def exec_10_2_9(org , tax):
	"""
	사용자로부터 소계와 팁 비율(0 ~ 100 사이의 값)을 입력받고 팁과 총계를 계산하는 파이썬 프고르맹을 작성하여라.
	예을 들어 , 사용자가 3000 과 10을 각각 입력하면 파이썬 프로그램은 '팁은 300원이고 , 총계는 3300원입니다.'
	를 출력
	"""
	tax_per = tax/100
	org_tax = org*tax_per
	return (org + org_tax , org_tax)


def exec_10_2_10(product1 , product2 , produce3):
	"""
	세 개 상품에 대한  세전 가격을 각각 입력하고 , 각 상품의 세후 가격과 세 상품의 평균
	가격을 계산하는 프로그램 작성
	단 , 부가가치세는 20%
	"""
	from decimal import getcontext , Decimal
	tax_per = 0.20
	total = 0
	for product in [product1 , product2 , produce3]:
		tax_prod = product * tax_per
		print('{} --> {}'.format(product , product + tax_prod))
		total += product + tax_prod


	getcontext().prec = 2

	print('average : {}'.format(float(Decimal(total/3))))



def exec_10_2_13(kwh):
	"""
	한달간 사용한 전력 소비랭 (kwh단위)을 입력받고 , kWh당 600원을 지불하는 경우 총 전기요금을 
	계산하는 파이썬 프로그램을 작성하여라. 단 , 부가가치세는 20%라고 가정한다.
	"""
	tax_per = 0.20
	useKwh = kwh * 600
	tax_prod = useKwh * tax_per
	return useKwh + tax_prod


def exec_10_2_14(month , day):
	"""
	사용자로부터 두 개의 숫자 (각각 월과 일을 의미)를 입력받고 , 1월1일부터 경과된 총 일수
	를 계산하는 파이썬 프로그램을 작성하여라. 단 , 한 달은 30일이라고 가정한다.
	"""
	pass





if __name__ == '__main__':
	
	# a = float(input('price :'))
	# b = float(input('sale : '))
	# result = exec_10_2_2( a  , b )
	

	# org = float(input('price :'))
	# result = exec_10_2_2(org)
	# print(' result : {}'.format(result))



	# org = float(input('price :'))
	# tax = float(input('tax :'))
	# result = exec_10_2_9(org , tax)
	# print(' result : {}'.format(result))


	# org1 = float(input('price1 :'))
	# org2 = float(input('price2 :'))
	# org3 = float(input('price3 :'))
	# exec_10_2_10(org1 , org2 , org3)


	org1 = float(input('use kwh :'))
	result = exec_10_2_13(org1)
	print(' result : {}'.format(result))



