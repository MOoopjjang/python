#!python
#-*- coding:utf-8 -*-



from decorator_module import print_decorator



@print_decorator(dp = False)
def exam_032():
	"""
	1,2차원 배열로 위도 , 경도 표현하기
	"""
	seoul_latitude1 = 37.52127220511242
	seoul_longitude1 = 127.0074462890625
	busan_latitude1 = 35.52127220511242
	busan_longitude1 = 129.0074462890625 

	seoul_info = list([seoul_latitude1 , seoul_longitude1])
	busan_info = list([busan_latitude1 , busan_longitude1])

	info = []
	info.append(seoul_info)
	info.append(busan_info)
	
	for v in info:
		print('%s - %s'%(v[0] , v[1]))



def exam_033():
	"""
	객체를 통한 위도 , 경도 표현
	"""
	@print_decorator('Geo' , True)
	class Geo:
		def __init__( self , l , r ):
			self.l = l
			self.r = r

		def getattr( self ):
			members = [ k+':'+str(self.__dict__[k]) for k in self.__dict__.keys() if k.startswith('__') == False and k.endswith('__') == False]
			return ','.join(members)	

		def __str__( self ):
			return '[ %s ] - %s '%(self.__class__.__name__ , self.getattr())


	seoul = Geo(37.52127220511242 , 127.0074462890625)
	busan = Geo(35.52127220511242 , 129.0074462890625)

	print('seoul :%s'%seoul)
	print('busan :%s'%busan)


def exam_035():
	"""
	3항 연산자를 사용하여 짝 , 홀 구분하기
	"""
	Num = 99
	for v in range(1,Num):
		result = '%d is 짝'%v if v%2 == 0 else '%d is 홀'%v
		print(result)


def exam_040():
	"""
	입력받은 문자열에 따라 달러 , 엔  , 위안을 한화로 환전해 보자.
	"""

	money_info = {
		"usd" : 1127.0
		,"jpy" : 1006.7
		,"cny" : 168.1
	}

	input_1 = input('usd( 달러) , jpy(엔화)  , cny(위안화):')
	input_2 = input('금액을 입력하세요:')
	print('input1 : '+input_1+" , input_2 : "+input_2)

	print('%s : %d ==> won : %.1f'%(input_1.lower() , int(input_2) , float(money_info[input_1.lower()])*int(input_2)))


def exam_043():
	"""
	while을 이용하여 1일 될때까지 나누고 곱하기

	입력된 수가 1이 될때까지 홀수는 3배+1 , 짝수는 2로 나눠보자
	"""

	input_1 = input('숫자를 입력하세요?')
	num = int(input_1)
	while True:
		v = num/2 if num%2 == 0 else num*3+1
		print('v : %d'%v)
		if v == 1:break
		num = v


def exam_046():
	"""
	while을 이용하여 서로 다른 세 정수 만들기

	서로 다른 세정수를 만들어 보자
	"""

	import random
	s = set()
	while True:
		rand = random.randint(1,100)
		if rand not in s:s.add(rand)
		if len(s) == 3:break

	print('s : %s'%s)

def exam_048():
	"""
	while과 단축 연산자를 이용하여 각 자릿수의 합 구하기

	특이사항 : pytho3.x에서는 정상적인 연산이 되지 않음.
	"""
	div_num = 10
	# mod_num = 1

	input_1 = input('input num:')
	num = int(input_1)
	v = 0
	while True:
		v += (num%div_num)
		num/=div_num
		if num < div_num:
			v += num
			break;

	
	print('v : %d'%v)



def exam_051():
	"""
	&(비트)연산자를 이용하여 2진수 문자열로 바꾸기
	&(비트) 연산자를 이용하여 10진수 정수를 2진수 문자열로 변환해 보자.
	"""
	BIT = 32
	BIT_MOVE = 1
	num = int(input('num:'))
	bit_str = ''
	for i in range(0 , BIT):
		bit_str+='0' if (num&(BIT_MOVE<<i) == 0) else '1'

	end = len(bit_str)-1
	rvr_str = ''
	while end > -1:
		rvr_str += bit_str[end]
		end -=1


	print('bit_str : %s'%bit_str)
	print('rvr_str : %s'%rvr_str)


def exam_051_1():
	"""
	&(비트)연산자를 이용하여 2진수 문자열로 바꾸기
	&(비트) 연산자를 이용하여 10진수 정수를 2진수 문자열로 변환해 보자.
	"""
	BIT = 32
	BIT_MOVE = 1
	num = int(input('num:'))
	bit_str = ''
	for index in range(0 , BIT):
		bit_str += '0' if (BIT_MOVE&(num>>index)) == 0 else '1'

	print('bit_str : %s'%bit_str)



def exam_052():
	"""
	문자열 자르기를 이용하여 2진수 문자열로 바꾸기
	불필요한 0을 제거한다.
	"""
	BIT = 32
	BIT_MOVE = 1
	num = int(input('num:'))
	bit_str = ''
	for i in range(0 , BIT):
		bit_str += '0' if (num&(BIT_MOVE<<i)) == 0 else '1'

	r_str = ''
	index = len(bit_str)-1
	while index > -1:
		r_str += bit_str[index]
		index -=1

	print('r_str : %s'%r_str)
	v = r_str[r_str.index('1'):]
	print('v : %s'%v)


def exam_58():
	"""
	for와 if를 용ㅇ하여 홀수에 대한 제곱의 합 구하기
	1 ~ 10사비의 홀수에 대한 제곱의 합을 구해보자.
	"""
	import math
	su= sum(list(map(lambda x:math.sqrt(x) , list(filter(lambda x:x%2 != 0 , range(1,10))))))
	print('su : %s'%su)

		

def exam_59():
	"""
	map을 이용하여 홀수의 합을 구하기
	1 ~ ₩00사이희 홀수의 합을 구해보자
	"""

	s = sum(list(filter(lambda x:x%2 ==1 , range(1,100))))
	print('s : %d'%s)

	l = sum([ i for i in range(1,100) if i%2==1 ])
	print('l : %d'%l)


def exam_060():
	"""
	Stream과 map을 이용하여 홀수에 대한 제곱의 합 구하기

	stream과 map을 이용하여 1 ~ 10 사이의 홀수에 대한 제곱의 합을 구해 보자
	"""
	ss = sum(list(map(lambda x:x**2,list(filter(lambda x:x%2 == 1 , range(1 , 10)))) ))
	print('exam_060 : %d'%ss)


def exam_061():
	"""
	String과 char를 이용하여 10진수를 2진수로변환하기

	String과 char를 이용하여 10진수를 2진수로 변환해 보자
	"""
	pass


def exam_067():
	"""
	String(문자열) 가공하기

	문자열의 길이 , 위치 등 문자열 관련 메서드를 익혀보자.
	"""
	strr = 'kknda,bakdoekkd,123'

	print(strr[10])
	strr_l = list(strr)
	print('strr_l : %s'%strr_l)
	strr_l[10] = 'C'
	print('strr_l : %s'%strr_l)
	c_strr = ''.join(strr_l)
	print('c_strr : %s'%c_strr)

	index = c_strr.index('C')
	print('index : %d'%index)
	# print('c_strr : %s'%c_strr[len(c_strr):0])
	print('-'*20+'reverse')
	index = len(c_strr)-1
	rStr = ''
	while index > -1:
		rStr += c_strr[index]
		index -=1

	print('rStr : %s'%rStr)
	print('-'*20+'partial reverse')
	index = 0
	start_idx = -1
	partial_str = ''
	while index < len(c_strr):
		if c_strr[index] == ',':
			end_idx = index-1
			while end_idx > start_idx:
				partial_str += c_strr[end_idx]
				end_idx -= 1
			partial_str+=','
			start_idx = index
		index += 1
		if index == len(c_strr):
			end_idx = index-1
			while end_idx > start_idx:
				partial_str += c_strr[end_idx]
				end_idx -= 1

	print('partial_str : %s'%partial_str)




def main():
	# exam_032()
	# exam_033()
	# exam_035()
	# exam_040()
	# exam_043()f
	# exam_046()
	# exam_048()
	# exam_051();
	# exam_051_1()
	# exam_052()

	# exam_58()
	# exam_59()
	# exam_060()

	exam_067()


if __name__ == '__main__':
	main()
