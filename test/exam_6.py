#!python3
#-*- coding:utf-8 -*-

#Introducing Python 연습문제



class Thing:
	def __init__(self):
		print('Thing  __init __')



class Element:
	def __init__(self , name , symbol , number):
		self.__name = name
		self.__symbol = symbol
		self.__number = number


	def __str__(self):
		return self.name+':'+self.symbol+":"+str(self.number)

	@property
	def name(self):
		return self.__name

	@name.setter	
	def name(self , _name):
		self.__name = _name

	@property
	def symbol(self):
		return self.__symbol

	@symbol.setter
	def symbol(self , _symbol):
		self.__symbol = _symbol

	@property
	def number(self):
		return self.__number

	@number.setter
	def number(self , _number):
		self.__number = _number

		

# 문자열 테스트
def t_string():
	# snowman = '\u2603'
	# print('{} : len {}'.format(snowman , len(snowman)))

	# ds = snowman.encode('ascii' , 'replace')
	# print('utf-8 ==> {} : len {}'.format(ds , len(ds)))

	# place = 'caf\u00e9'
	# print(' ==> {} : len {}'.format(place , len(place)))

	# place_byte = place.encode('utf-8')
	# print(' place_byte {} : len {}'.format(place_byte , len(place_byte)))
	# place2 = place_byte.decode('utf-8')
	# print(' place2 {} : len {}'.format(place2 , len(place2)))

	# place3 = place_byte.decode('ascii')


	n = 42
	f = 7.03
	s = 'string cheese'

	print('n:{} , f:{} , s:{}'.format(n , f , s))

	d={'n':42 , 'f':7.03 , 's':'string cheese'}
	print('{0[f]} {0[n]} {0[s]} {1}'.format(d , 'other'))


def main():
	#6-1
	# example = Thing()
	# print('{} : {}'.format(example , Thing)) 

	#6.4
	# sixafour = Element('Hydrogen' , 'H' ,1)

    #6.5
    # el_dict = {'name':'xferlog' , 'symbol':'H' , 'number':1}
    # print('{}'.format(el_dict))
    # k = Element(**el_dict)
    # print('{}'.format(k))

    # print(k.name)
    # k.name = 'kknda'
    # print(k.name)


	t_string()


if __name__ == '__main__':
	main()





