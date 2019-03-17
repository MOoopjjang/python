#!python
#-*- coding:utf-8 -*-


"""
파일 rangetest_test.py
주석 처리된 줄은 셀 명령 라인에서 "python -O"을 사용하지 않으면 TypeError발생
"""

from __future__ import print_function #2.x
from rangetest import rangetest

# 함수 테스트 : 위치와 키워드 인수

@rangetest(age = (0 , 120))
def persinfo(name , age):
	print('%s is %s years old'%(name , age))

@rangetest(M = (1 , 12) , D=(1,31) , Y = (0 , 2013))
def birthday(M , D , Y):
	print('birthday = {0}/{1}/{2}'.format(M , D , Y))




#메소드 테스트 : 위치와 키워드 인수
class Person:
	def __init__( self , name , job , pay):
		self.job = job
		self.pay = pay

	@rangetest(percent=(0.0 , 1.0))
	def giveRaise( self , percent ):
		self.pay = int(self.pay * (1+percent))


#생략된 기본 인수 테스트 : 생략
@rangetest(a = (1 , 10) , b=(1 , 10) , c=(1,10) , d=(1,10))
def omitargs(a , b=7 , c=8 , d=9):
	print(a , b , c , d)


if __name__ == '__main__':
	persinfo('Bob' , 40)
	persinfo(age = 40 , name='Bob')
	birthday(5 , D=1 , Y=1963)
	# persinfo('Bob' , 150)
	# persinfo(age = 150 , name = 'Bob')
	# birthday(5 , D=40 , Y=1963)

	print('-'*100)
	bob = Person('Bob Smith' , 'dev' , 100000)
	sue = Person('Sue Jones' , 'dev' , 100000)
	bob.giveRaise(.10)
	sue.giveRaise(percent = .100)
	print(bob.pay , sue.pay)
	#bob.giveRaise(1.10)
	#bob.giveRaise(percent = 1.20)


	print('-'*100)
	omitargs(1,2,3,4)
	omitargs(1,2,3)
	omitargs(1,2,3,d=4)
	omitargs(1,d=4)
	omitargs(d=4 , a=1)
	omitargs(1 , b=2 , d=4)
	omitargs(d=8 , c=7 , a=1)

	# omitargs(1,2,3,11)
	# omitargs(1,2,11)









