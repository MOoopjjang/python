#!python3
#-*- coding:utf-8 -*-


import requests

def main():
	print('test main called!!!')

	res = requests.get('http://www.naver.com' , timeout = 5)
	res.raise_for_status()
	print(res.text)


if __name__ == '__main__':
	main()