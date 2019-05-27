#!python3
#-*- coding:utf-8 -*-




"""
retry test
"""


import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError
from requests.packages.urllib3.util.retry import Retry

GIT_URL1 = 'https://api.github.com'
TST_URL1 = 'http://localhost:8080/test/sample'




def retry_session():
	session = requests.Session()
	retry = Retry(
		total=3,
		read = 3,
		backoff_factor = 3,
		status_forcelist = (500 , 502 , 504),
		method_whitelist = ('GET' , 'POST')
		)

	adapter = HTTPAdapter(max_retries = retry)
	session.mount('http://' , adapter)
	session.mount('https://' , adapter)
	return session


def tst1():
	github_adapter = HTTPAdapter( max_retries = 10 )
	session = requests.Session()

	session.mount('http://' , github_adapter )
	try:
		session.get(TST_URL1)
	except ConnectionError as ce:
		print(ce)


def tst2():
	session = retry_session()
	try:
		print('a')
		session.get(TST_URL1 )
		print('b')
	except ConnectionError as ce:
		print(ce)



if __name__ == '__main__':
	# tst1()
	tst2()









