#!python

"""
classtree.py:네임스페이스 링크를 이용해 인스턴스 트리를 거슬러 올라가며,
상위의 슈퍼클래스를 클림함,들여쓰기를 이용해 높이를 표시.
"""


def classtree( cls , indent ):
	print('.' * indent + cls.__name__)
	for supercls in cls.__bases__:
		classtree( supercls , indent+3 )

def instancetree( inst ):
	print('Tree of %s' % inst )
	classtree( inst.__class__ , 3 )


def selftest():
	class A:pass
	class B( A ):pass
	class C( A ):pass
	class D(B , C):pass
	class E:pass
	class F(D,E):pass
	instancetree(B())
	instancetree(F())


if __name__ == '__main__':
	selftest()