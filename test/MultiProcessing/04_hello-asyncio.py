#!python3
#-*- coding:utf-8 -*-


import asyncio


async def hello_world():
	print('hello world')
	return 42



h_w_coroutine = hello_world()
print(h_w_coroutine)
event_loop = asyncio.get_event_loop()
try:
	print('entring event loop')
	result = event_loop.run_until_complete(h_w_coroutine)
	print(result)
finally:
	event_loop.close()

# def main():



# if __name__ == '__main__':
# 	main()
