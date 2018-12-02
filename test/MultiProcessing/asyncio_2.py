#!python3
#-*- coding:utf-8 -*-



import asyncio


@asyncio.coroutine
def hello_world():
	yield from asyncio.sleep(1)
	print('Hello World')
	asyncio.async(hello_world())


@asyncio.coroutine
def good_evening():
	yield from asyncio.sleep(1)
	print('Good Evening')
	asyncio.async(good_evening())

def main():
	print(' step : asyncio.get_event_loop()')
	loop = asyncio.get_event_loop()
	try:
		print(' step : loop.run_until_complete()')
		asyncio.async(hello_world())
		asyncio.async(good_evening())
		loop.run_forever()
	except KeyboardInterrupt:
		pass
	finally:
		print('step : loop.close()')
		loop.close()


if __name__ == '__main__':
	main()