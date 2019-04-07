#!python3
#-*- coding:utf-8 -*-



import asyncio
from aiohttp import ClientSession


BASE_URL = 'http://httpbin.org/get?'


"""
  url_get : 동기방식 + one thread
  mt_url_get : 동기방식 + 100 thread
  test_async_url_get : 비동기방식 + one thread

  result :
    async_test2_result.txt
"""


def ConsumeDecorator( func ):
	def onDecorator( *args , **kargv ):
		import timeit
		start = timeit.default_timer()
		r = func(*args , **kargv)
		print('[%s] duration time %s'%(func.__name__ , timeit.default_timer() - start))
		return r
	return onDecorator


@ConsumeDecorator
def url_get():
	import requests
	for i in range(100):
		res = requests.get(BASE_URL+str(i))
		# print(' get i : %d'%i)



def url_get_2(url):
	import requests
	res = requests.get(url)
	# print(' get i : %s'%url)

@ConsumeDecorator
def mt_url_get():
	import concurrent.futures
	from concurrent.futures import ThreadPoolExecutor

	with ThreadPoolExecutor(max_workers = 100) as executors:
		futures = [ executors.submit(url_get_2 , BASE_URL+str(i)) for i in range(100) ]
		for f in concurrent.futures.as_completed(futures):
			f.result()
	print('end')



async def async_url_get(url):
	async with ClientSession() as session:
		async with session.get(url) as response:
			r = await response.read()
			# print(r)




@ConsumeDecorator
def test_async_url_get():
	loop = asyncio.get_event_loop()
	tasks = []
	for i in range(100):
		task = asyncio.ensure_future(async_url_get(BASE_URL+str(i)))
		tasks.append(task)
	loop.run_until_complete(asyncio.wait(tasks))




	# from threading import Thread
	# threads = [ Thread(target = url_get_2 ,args=(BASE_URL+str(i),)) for i in range(100) ]
	# for thread in threads:
	# 	thread.start()
	# for thread in threads:
	# 	thread.join()
		


if __name__ == '__main__':
	# url_get()
	# mt_url_get()
	test_async_url_get()



