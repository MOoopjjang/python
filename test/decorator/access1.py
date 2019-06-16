#!python
#-*- coding:utf-8 -*-


"""
클래스 인스턴스로부터 가져오는 속성을 위한 프라이버시 사용 예시로
파일 마지막의 셀프 테스트 코드를 참조할 것

다음과 동일한 데코레이터:Doubler = Private('data' , 'size')(Doubleer)
Private은 onDecorator를 반환하고 , onDecorator는 onInstance를 반환하며,
각 onInstance의 인스턴스는 Doubler 인스턴스를 내장함.

소스코드 이해도 :
    90%
"""


traceMe = False


def trace( *args ):
	if traceMe:print('['+' '.join(map(str , args))+']')


def Privates( *privates ):
	def onDecorator( aClass ):
		class onInstance:
			def __init__( self , *args , **kargv ):
				self.wrapped = aClass( *args , **kargv )

			def __getattr__( self , attrname ):
				trace('__getattr__ ' , attrname)
				if attrname in privates:
					raise TypeError('%s is private member'%attrname )
				else:
					return getattr(self.wrapped , attrname)

			def __setattr__( self , attrname , value ):
				trace('__setattr__ ' , attrname , value)
				if attrname == 'wrapped':
					self.__dict__[attrname] = value
				elif attrname in privates:
					raise TypeError('%s is private member'%attrname )
				else:
					setattr( self.wrapped , attrname , value )

		return onInstance
	return onDecorator



if __name__ == '__main__':
	traceMe = True
	@Privates('name' , 'age')     				# private 멤버로 'name' , 'age'를 지정한다. onDecorator를 반환
	class Person:								
		def __init__( self , name , age ):
			self.name = name
			self.age = age

		def getName( self ):return self.name
		def getAge( self ):return self.age



	person = Person('cwkim' , 40)			# person =  [[  onDecorator(Person) -> onInstance('cwkim' , 40)  ]]
	print('name : '+person.getName())		# __getattr__ -> getattr(self.wrapped , attrname)
	print('age :'+person.age)				# __getattr__ -> ypeError('%s is private member'%attrname )





















