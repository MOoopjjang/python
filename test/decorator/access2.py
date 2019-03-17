#!python
#-*- coding:utf-8 -*-

"""
Private 과 Public속성 선언을 가진 클래스 decorator

인스턴스에 저장되었거나 또는 그 인스턴스가 자신의 클래스로부터 상속받은 속성에 대하여
외부로부터의 접근을 제어함.Private은 데코레이트된 클래스 외부에서 가져올 수도 할당할 수도 없는
속성 이름을 선언하고 Public은 이 모든 것이 가능한 이름을 선언함

경고 : 이는 3.x에서 명시적으로 지정된 속성에 대해서만 동작함.
내장 연상을 위해 암묵적으로 실해오디는 __X__연산자 오버로딩 메서드는 새 형식 클래스에서 
__getattr__ 또는 __getatttribute__모두 동작시키지 않음.여기에서 내장을  가로채고 위함하기 위해
__X__메서드를 추가함.

소스코드 이해도 : 0%
"""


traceMe = False

def trace(*args):
	if traceMe:print('['+' '.join(map(str , args)) +']')


def accessControl( failIf ):
	def onDecorator( aClass ):
		# class onInstance:
		# 	def __init__( self , *args , **kargs):
		# 		self.__wrapped = aClass(*args , **kargs )

		# 	def __getattr__( self , attr ):
		# 		trace('get : '+attr)
		# 		if failIf(attr):
		# 			raise TypeError('private attribute fetch: '+attr)
		# 		else:
		# 			return getattr(self.__wrapped , attr )

		# 	def __setattr__( self , attr , value ):
		# 		trace('set : ',attr , value)
		# 		if attr == '_onInstance__wrapped':
		# 			self.__dict__[attr] = value
		# 		elif failIf(attr):
		# 			raise TypeError('private attribute change : '+attr)
		# 		else:
		# 			setattr(self.__wrapped , attr , value)
		# return onInstance


		def getattributes( self , attr ):
			trace('get : ',attr)
			if failIf( attr ):
				raise TypeError('private attribute fetch : '+attr)
			else:
				return object.__getattribute__( self , attr )

		def setattributes( self , attr , value ):
			trace('set : ' , attr)
			if failIf( attr ):
				raise TypeError('private attribute change: '+attr )
			else:
				return object.__setattr__( self , attr , value )

		aClass.__getattribute__ = getattributes
		aClass.__setattr__ = setattributes
		return aClass
	return onDecorator


def Private( *attributes ):
	return accessControl(failIf=(lambda attr:attr in attributes))

def Public( *attributes ):
	return accessControl(failIf = (lambda attr:attr not in attributes))


if __name__ == '__main__':
	@Private('age')
	class Person:
		def __init__( self , name , age):
			self.name = name
			self.age = age



	p = Person('xferlog' , 10)
	print(p.name)
	print(p.age)






