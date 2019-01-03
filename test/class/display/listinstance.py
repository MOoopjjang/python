#!python


class ListInstance:
	"""
	여기에서 작성된 __str__의 상속을 통해 인스턴스의 포맷이 갖춰진
	print()또는 str()을 제공하는 혼합 클래스,self는 가장 낮은 클래스의 인스턴스임
	__X 이름은 클라이언트의 속성과의 충돌을 피함 
	"""
	def __attrnames( self ):
		result = ''
		for attr in sorted(self.__dict__):
			result += '\t%s=%s\n'%(attr,self.__dict__[attr])
		return result

	def __str__( self ):
		return '<Instance of %s , address %s:\n%s'%(self.__class__.__name__ ,id(self) , self.__attrnames())


if __name__ == '__main__':
	ListInstance
