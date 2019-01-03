#!python


"""
일반적인 리스터 혼합 테스터:25장의 리로드 도구와 유사하지만 , 테스터에 클래스 객체를 전달함(함수가 아니라).
그리고 testByNames는 31장의 팩토리 패턴에 따라 여기에서 이름 문자열로 모듈과 클래스를 로딩하는 것을 추가함.
"""

import importlib

def tester(listerclass , sept=False):
	class Super:
		def __init__( self ):
			self.data1 = 'spam'
		def ham( self ):pass


	class Sub( Super , listerclass):
		def __init__( self ):
			Super.__init__( self )
			self.data2 = 'ppp'
			self.data3 = 30
		def spam( self ):pass


	instance = Sub()
	print(instance)
	if sept:print('-'*80)


def testByNames(modname , classname , sept = False):
	modobject = importlib.import_module(modname)
	listerclass = getattr( modobject , classname )
	tester( listerclass , sept)


if __name__ == '__main__':
	testByNames('listinstance' , 'ListInstance' , True )
	testByNames('listinherited' , 'ListInherited' , True )
	testByNames('listtree' , 'ListTree' , True )
