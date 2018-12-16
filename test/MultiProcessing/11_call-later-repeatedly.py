#!python3
#-*- coding:utf-8 -*-


import asyncio

el = asyncio.get_event_loop()

async def hello_world():
	el.call_later(1 , hello_world)
	print('hello_world')


el = asyncio.get_event_loop()
el.call_later(1 , hello_world)
el.run_forever()
