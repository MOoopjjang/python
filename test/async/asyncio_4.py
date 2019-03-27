#!python3
#-*- coding:utf-8 -*-



import asyncio
import random


"""
결과만 취합하기
code : result = await asyncio.gather(*fts)
"""


async def lazy_greet( msg , delay = 1):
	print('lazy_greet : {} '.format(msg))
	await asyncio.sleep(delay)
	return msg


async def time_log():
	i = 0
	print('start time_log')
	while True:
		await asyncio.sleep(1)
		i +=1
		print('..%02d sec'%i)


async def main():
	t = asyncio.ensure_future(time_log())
	msgs = ['xferlog' , 'kknda' , 'bhkim' , 'hi']
	fts = [ asyncio.ensure_future(lazy_greet(m , random.randint(1 , 5))) for m in msgs ]
	result = await asyncio.gather(*fts)
	t.cancel()
	print(result)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
