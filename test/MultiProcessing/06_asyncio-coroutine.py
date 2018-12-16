#!python3
#-*- coding:utf-8 -*-

import asyncio



async def plus( num ):
	print('plus : {}'.format( num ))
	return num+42


async def hello_world():
	print(' hello_world')
	result = await plus( 24 )
	return result



event_loop = asyncio.get_event_loop()
try:
	print(' event looping...')
	result = event_loop.run_until_complete(hello_world())
	print('result : {}'.format(result))
finally:
	event_loop.close()

