#!python
#-*- coding:utf-8 -*-



class Wrapped:
	def __init__( self , _obj ):
		self._obj = _obj

	def __iter__( self ):
		for o in self._obj:
			yield o


	def __getattr__( self , attrname ):
		print('attr : {}'.format(attrname))
		return getattr(self._obj , attrname )



def tst_1():
	w = Wrapped(['a','b','c'])
	w.append('d')

	for d in w:print(d)


	w = Wrapped({'name':'k' , 'age':30})
	print(w.keys())




if __name__ == '__main__':
	tst_1()
