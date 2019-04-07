#!python
#-*- coding:utf-8 -*-



import asyncio
import aiohttp

async def fetch_page(session , url ):
	async with session.get(url) as response:
		return await response.text()




async def main():
	async with aiohttp.ClientSession() as session:
		html = await fetch_page(session , 'http://python.org')
		print(html)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())		
