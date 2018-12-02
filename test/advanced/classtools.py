#!python3
#-*- coding:utf-8 -*-



class AttrDisplay:
	"""
	상속 가능한 디스플레이 오버로드 메서드를 제공
	이 메서드는 인스턴스를 이들의 클래스 이름과 함께 그 인스턴스에 저장된 각 속성을 이름=쌍으로 보여 줌
	(하지만 그 인스턴스의 클래스로부터 상속받은 속성을 보여 주지는 않음)
	어떤 클래스에도 혼합될 수 있으며 , 어떤 인스턴스에서도 동작함.
	"""
	def __gatherAttr( self ):
		attrs = []
		for key in sorted( self.__dict__):
			attrs.append('{}={}'.format(key , self.__dict__[key]))
		return ','.join(attrs)

	def __repr__( self ):
		return '[{}]{}'.format(self.__class__.__name__ , self.__gatherAttr())




