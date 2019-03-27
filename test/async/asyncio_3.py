#!python3
#-*- coding:utf-8 -*-


import asyncio
import random


async def lazy_greet(msg , delay = 1 ):
	print(msg , 'will be displayed in' , delay , ' seconds')
	await asyncio.sleep(delay)
	return msg


async def main():
	msgs = ['xferlog' , 'kknda' , 'bhkim' , 'hi']
	fts = [ asyncio.ensure_future(lazy_greet(m , random.randint(1,5))) for m in msgs ]
	(done , pending) = await asyncio.wait(fts , timeout = 2)

	if pending:
		print('pending : {}'.format(len(pending)))

		for f in pending:
			f.cancel()

	for f in done:
		x = await f
		print("x : {}".format(x))





loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
