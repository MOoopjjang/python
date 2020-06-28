#!python3
#-*- coding:utf-8 -*-


'''
 객체의 멤버의 값을 출력해준다
 - 단독으로 동작하지 않고 상속을 해야 동작한다.
'''

from abc import ABCMeta , abstractmethod

class MPWAttribute( metaclass = ABCMeta ):
	def getMpwAttribute( self , *exclude ):
		# 내장멤버 ( __dict__)를 통하여 클래스멤버의 정보를 String형태로 반환한다.
		# *exclude에 포함된 항목은 출력하지 않는다.
		 return '#'.join(['{}:{}'.format(k,str(v)) for k,v in self.__dict__.items() if k not in exclude])
