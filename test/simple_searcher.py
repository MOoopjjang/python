#!python3
#-*- coding:utf-8 -*-


import requests

def main():
	session = requests.session();
	res = session.get('http://www.naver.com' , timeout = 3);
	res.raise_for_status()
	print('{}'.format(res.text))


if __name__ == '__main__':
	main();