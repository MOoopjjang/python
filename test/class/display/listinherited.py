#!python

class ListInherited:
	"""
	dir()을 사용하여 인스턴스 속성과 그 인스턴스의 클래스로부터 상속방은 이름을 수집.
	python 3.x는 2.x보다 더 많은 이름을 보여 주는데 새 형식 클래스 모델에서
	암묵적인 슈퍼클래스인 object때문임. self.__dict__가 아니라 getattr()에서 상속된 이름을 가져옴.
	___repr__이 아니라 __str__을 사용할 것. 그렇지 않으면 바운드 메서드를 출력할 때 루프가 발생하게 됨!
	"""
	def __attrnames( self ):
		result = ''
		for attr in dir(self):
			if attr[:2] == '__' and attr[-2:] == '__':
				result += '\t%s\n' % attr
			else:
				result += '\t%s=%s\n'%(attr,getattr(self , attr))
		return result


	def __str__( self ):
		return 'Instance of %s , address %s:\n%s'%(self.__class__.__name__ , id(self) , self.__attrnames())


if __name__=='__main__':
	import testmixin
	testmixin.tester(ListInherited)
