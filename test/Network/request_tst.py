#!python3
#-*- coding:utf-8 -*-


import requests


TEST_URL_1 = 'http://localhost:8080/test/'


def parsing(_res):
	print('url : '+_res.url)
	print('response_code :'+str(_res.status_code ))
	print('response_body==')
	print(_res.json())
	print('encoding : '+_res.encoding)
	print('headers : ')
	print(_res.headers)

def test_1():
	url = TEST_URL_1+"/sample"
	res = requests.get(url)
	parsing(res)


def test_get_param():
	# 1
	fullUrl = TEST_URL_1 + '/sample/1?name=xferlog&age=20'
	res = requests.get(fullUrl)
	parsing(res)


def test_get_headers():
	params = {}
	params['name'] = 'xferlog'
	params['age'] = 20

	headers = {}
	headers['Content-Type'] = 'application/json'

	url = TEST_URL_1 + '/sample/1'
	res = requests.get(url , params = params , headers = headers)
	parsing(res)


def test_get_timeout():
	times = (3 , 3)
	params = {}
	params['name'] = 'xferlog'
	params['age'] = 20

	headers = {}
	headers['Content-Type'] = 'application/json'

	url = TEST_URL_1 + '/sample/1'
	res = requests.get(url , params = params , headers = headers , timeout = times )
	parsing(res)



def test_post():
	import json
	url = TEST_URL_1 + '/sample/1'
	data ={}
	data['name'] = 'xferlog'
	data['age'] =20

	params = json.dumps(data)

	headers = {}
	headers['Content-Type'] = 'application/json'

	res = requests.post(url = url , data = params , headers = headers)
	parsing(res)



def test_delete():
	url = TEST_URL_1 + '/sample/1'
	res = requests.delete(url)
	parsing(res)


def test_put():
	import json
	url = TEST_URL_1 + '/sample/1'

	headers = {'Content-Type':'application/json'}
	data = {'name':'xferlog','age':20}
	params = json.dumps(data)
	res = requests.put(url , data = params , headers = headers)
	parsing(res)


def test_head():
	''' requests로 HEAD 요청을 만들고 응답으로부터 헤더를 추출하는 예제'''

	resp = requests.head('http://www.naver.com')
	#print(resp.text)


	for h in resp.headers.keys():
		print('{}'.format(h))

	content_type = resp.headers['Content-Type']
	content_date = resp.headers['Date']
	# content_length = resp.headers['content-length']
	print('status : {}'.format(resp.status_code))
	print('date : {}'.format(content_date))
	print('ct : {}'.format(content_type))
	# print('cl: '.format(content_length))

if __name__ == '__main__':
	# test_1()
	# test_get_headers()
	# test_get_timeout()

	# test_post()

	# test_delete()

	# test_put()
	test_head()

