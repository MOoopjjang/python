#!python3
#-*- coding:utf-8 -*-


import requests
import bs4



def t1():
	session = requests.session();
	res = session.get('https://nbamania.com/g2/bbs/board.php?bo_table=nbatalk&r=ok' , timeout = 3)
	res.raise_for_status()
	# print('body : {}'.format(res.text))
	bsObj = bs4.BeautifulSoup(res.text , 'html.parser')

	ems = bsObj.findAll('a' , {'class':'list_subject_a'})
	for index , e in enumerate( ems ):
		title = e.find('font' , {'class':'mobile_hide'})
		print('{}.{}'.format(index , title.get_text().strip()))





def main():
	t1()

if __name__ == '__main__':
	main()