#!python
#-*- coding:utf-8 -*-


import requests
import re
import bs4
import operator


filterList = ['the' , 'be' , 'and' , 'of' , 'a' , 'in' , 'to' , 'have' , 'has','it' , 'that' , 'i' , 'for'
,'was','not','he','her']

def convertLineToSpace( _text ):
	_text = re.sub('<\/?[\w\d].*?>' , '' , _text)  # tag 삭제
	_text = re.sub('<![\w-].+>' , '' , _text) # 주석 삭제
	_text = re.sub('&nbsp' , '' , _text)  # 공백삭제
	_text = re.sub('[^\w\d]' , ' ' , _text)  # 특수문자 삭제
	_text = re.sub('\n+' , ' ' , _text) # 줄넘김 -> 공백

	texts = _text.split(' ')
	convert = []
	for text in texts:
		if (' ' not in text.lower()) and (len(text.lower()) > 0) and (text.lower() not in filterList):
			convert.append( text.lower() )

	return convert


def makeSet( _datas , n ):
	m = {}
	for i in range( len(_datas )-n):
		key = ' '.join(_datas[i:i+n])
		if key not in m.keys():
			m[key] = 0
		m[key] +=1
	return m



def main():
	session  = requests.session()
	res = session.get('http://www.gnu.org/gnu/manifesto.en.html' , timeout = 3)
	res.raise_for_status()

	mm = makeSet( convertLineToSpace( res.text ) , 2)
	smm = sorted(mm.items() ,key = operator.itemgetter(1) , reverse = True)
	# print('{}'.format(mm))
	for m in smm:
		print('{}:{}'.format(m[0],m[1]))

if __name__ == '__main__':
	main()

