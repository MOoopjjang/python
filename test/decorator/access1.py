#!python
#-*- coding:utf-8 -*-


"""
클래스 인스턴스로부터 가져오는 속성을 위한 프라이버시 사용 예시로
파일 마지막의 셀프 테스트 코드를 참조할 것

다음과 동일한 데코레이터:Doubler = Private('data' , 'size')(Doubleer)
Private은 onDecorator를 반환하고 , onDecorator는 onInstance를 반환하며,
각 onInstance의 인스턴스는 Doubler 인스턴스를 내장함.

소스코드 이해도 :
    0%
"""


traceMe = False
def trace(*args):
	if traceMe:print('['+' '.join(map(str , args))+']')

def Private(*privates):
	def onDecorator( aClass ):
		class onInstance:
			def __init__( self , *args , **kargs ):
				self.wrapped = aClass(*args , **kargs)

			def __getattr__( self , attr ):
				trace('get:' , attr )
				if attr in privates:
					raise TypeError('private attribute fetch: '+attr)
				else:
					return getattr(self.wrapped , attr)

			def __setattr__( self , attr , value ):
				trace('set :',attr , value)
				if attr == 'wrapped':
					self.__dict__[attr] = value
				elif attr in privates:
					raise TypeError('private attribute change :'+attr)
				else:
					setattr(self.wrapped , attr , value )

		return onInstance
	return onDecorator



if __name__ == '__main__':
	traceMe = True

	@Private('data' , 'size')
	class Doubler:
		def __init__( self , label , start ):
			self.label = label
			self.data = start

		def size( self ):
			return len(self.data)

		def double( self ):
			for i in range(self.size()):
				self.data[i] = self.data[i]*2

		def display( self ):
			print('%s => %s'%(self.label , self.data))


	X = Doubler('X is' , [1,2,3])
	Y = Doubler('Y is' , [-10 , -20 , -30])


	# 다음은 모두 성공
	print(X.label)
	X.display();X.double();X.display()
	print(Y.label)
	Y.display();Y.double()
	Y.label = 'Spam'
	Y.display()

	# 다음은 모두 적절히 싪패함
	"""
	print(X.size())
	print(X.data)
	X.data = [1,1,1]
	X.size = lambda S: 0
	print(Y.data)
	print(Y.size())
	"""


















