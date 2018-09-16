#!python3
#-*- coding:utf-8 -*-


import requests


def test():
	params = {'firstname':'Ryan','lastname':'Mitchell'}
	session = requests.session()
	res = session.post('http://pythonscraping.com/pages/files/processing.php' , data = params)
	print('{}'.format(res.text))


def test2():
	from requests.auth import AuthBase
	from requests.auth import HTTPBasicAuth
	auth = HTTPBasicAuth('ryan' , 'password')
	r = requests.post(url = 'http://pythonscraping.com/pages/auth/login.php' , auth = auth)
	print(r.text)


def test3():
	header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Max OS X 10_9_5 } AppleWebKit 537.36 (KHTML , like Gecko ) Chrome'
	 , 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}

	# header = {'User-Agent':'MOoop/1.0'}
	res = requests.get('http://localhost:8080/sfp/user/email/kcwda@aaa.com' , headers = header)
	# res = requests.get('http://localhost:8080/sfp/user/email/kcwda@aaa.com' )
	res.raise_for_status()
	print('{}'.format(res.text))



def main():
	# test()
	# test2()
	test3()
	

if __name__ == '__main__':
	main()