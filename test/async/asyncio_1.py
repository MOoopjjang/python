#!python3
#-*- coding:utf-8 -*-



import asyncio



async def myCoroutine():
	print('Simple Event Loop Example')


# @asyncio.coroutine
async def greet(msg , delay=1):
	await asyncio.sleep(delay)
	print('msg : %s'%msg)


async def main():
	import random

	msgs = ['xferlog' , 'kknda' , 'bhkim' , 'hi']
	fts = [ asyncio.ensure_future(greet(m , random.randint(1,5))) for m in msgs ]
	for f in asyncio.as_completed(fts):
		x = await f
		print(x)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()


