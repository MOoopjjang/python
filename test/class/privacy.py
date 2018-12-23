#!python3
#-*- coding:utf-8 -*-


"""
Class별로 객체 생성시 예약속성을 정의하여 override를 방지하는 sample code...
"""


class Privacy:
	# def __init__( self , _private ):
	# 	print('_private : {}'.format(_private))
	# 	self.private = _private

	def __setattr__( self , attr , value ):
		print('__setattr__ : {}'.format(attr))
		if attr in self.private:
			raise Exception('Already {} exist!!!'.format(attr))
		else:
			self.__dict__[ attr ] = value



class Test1( Privacy ):
	private = ['age']
	# def __init__( self  ):
	# 	Privacy.__init__( self , ['age'])
		# super( Privacy , self).__init__(['age'])



class Test2( Privacy):
	def __init__( self  ):
		Privacy.__init__( self , ['age' , 'name'])



def main():
	t1 = Test1()
	t1.age = 'xferlog'



if __name__ == '__main__':
	main()


