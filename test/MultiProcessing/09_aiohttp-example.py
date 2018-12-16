#!python3
#-*- coding:utf-8 -*-


import asyncio
import aiohttp

async def get( _url ):
	async with aiohttp.ClientSession() as session:
		async with session.get( _url ) as response:
			return response



event_loop = asyncio.get_event_loop()
coroutines = [ get('http://www.naver.com') for _ in range(8)]	
results = event_loop.run_until_complete(asyncio.gather(*coroutines))
print(results)		