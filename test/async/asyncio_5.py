#!python3
#-*- coding:utf-8 -*-



import timeit
import asyncio
import datetime


def duration_decorator( func ):
	def onWrapped( *args , **kargv ):
		s = timeit.default_timer()
		r = func(*args , **kargv )
		print('[%s] duration : %s'%(func.__name__ , timeit.default_timer() - s))
		return r
	return onWrapped



async def func( _delay , msg ):
	print('msg start ')
	await asyncio.sleep(_delay)
	print('msg : {}'.format(msg))


async def display_date():
	loop = asyncio.get_running_loop()
	end_time = loop.time() + 5.0
	while True:
		print(datetime.datetime.now())
		if (loop.time() + 1.0) >= end_time:
			break
		await asyncio.sleep(1)


async def factorial(name , number ):
	f = 1
	for i in range(2 , number + 1):
		print(f'Task {name} : Compute factorial ({i})...')
		await asyncio.sleep(1)
		f *= i
	print(f'Task {name}: factorial ({number}) = {f}')



async def main():
	# tasks = [ asyncio.create_task(func(i , "hello : {}".format(i))) for i in range(1,3) ]
	# for task in tasks:await task

	await asyncio.gather(
		factorial('A' , 2),
		factorial('B' , 3),
		factorial('C' , 4)
		)


if __name__ == '__main__':
	# asyncio.run(main())
	# asyncio.run(display_date())


	asyncio.run(main())


