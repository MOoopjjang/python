#!python
#-*- coding:utf-8 -*-


from object_file_decorator import ObjectFileWriteDecorator
from singleton_decorator import singleton


@ObjectFileWriteDecorator( 'xferlog' , True )
class BillBoardChart:
	def __init__( self , rank , song , lastWeek , imageSrc , artistSrc , artist ):
		self._rank = rank
		self._song = song
		self._lastWeek = lastWeek
		self._imageSrc = imageSrc
		self._artistSrc = artistSrc
		self._artist = artist

	
	def __str__( self ):
		return '[%s] %s'%(self.__class__.__name__ , self.__getattribute())


	def __getattr__(self , attr):
		print('__getattr__ attr : %s'%attr)
		if attr not in ['rank' , 'song' , 'lastWeek' , 'imageSrc' , 'artistSrc' , 'artist']:
			raise TypeError('%s TypeError'%attr)
		else:
			return self.__dict__['_'+attr]

	def __setattr__( self , attr , value ):
		cAttr = attr
		if attr.startswith('_'):
			cAttr = attr[len('_'):]
		if cAttr not in ['rank' , 'song' , 'lastWeek' , 'imageSrc' , 'artistSrc' , 'artist']:
			raise TypeError('%s TypeError'%cAttr)
		else:
			self.__dict__[attr] = value

			
	def __getattribute( self ):
		l = ['%s:%s'%(k,self.__dict__[k]) for k in self.__dict__ 
		if (bool(k.startswith('__')) == False and bool(k.endswith('__')) == False)]
		return ','.join(l)




@singleton('BillBoardManager' , True)
class BillBoardManager:
	def __init__( self ):
		self._billboardList = []


	def put( self , data ):
		self._billboardList.append( data )


	def get( self , index ):
		return self._billboardList[ index ]

	def load( self  , _path ):
		import json
		with open(_path , 'r') as fr:
			lj = []
			for line in fr:
				dd = json.dumps(line[:-1])
				lj.append(json.loads(dd))
			print(lj)



def exam_082_088():
	"""
	billboard chart 정보를 객체에 저장 + 파일로 저장 + 파일 읽기 
	"""
	mgr = BillBoardManager()
	mgr.put(BillBoardChart(1 , 'you and i' , 3 , 'http://image' , 'http://blog' , 'kim'))
	mgr.put(BillBoardChart(2 , 'ccccc' , 3 , 'http://image/ccc' , 'http://blog/ccc' , 'cccc'))

	mgr.load('xferlog')



if __name__ == '__main__':
	exam_082_088()

	# mgr = BillBoardManager()
	# print(mgr)










