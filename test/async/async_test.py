#!python3


import requests
import timeit
import os

import asyncio
import aiohttp                  # asyncio를 사용하여 HTTP 요청을 하기 위해 사용합니다.
import aiofiles                 # asyncio를 사용하여 파일 입출력을 하기 위해 사용합니다.


"""
 async방식을 통한 download 속도 개선...
"""


def makedir( dirName ):
	os.mkdir(dirName)
	return dirName

def sync_download( dirName ):

	dName = makedir(dirName)
	os.chdir(dName)
	start = timeit.default_timer()
	for i in range(128):
		print('downloading... {}'.format(i))
		res = requests.get(f'http://www.randomtext.me/api/lorem/p-1/32')
		with open(f'{i}.txt' , 'w') as f:
			f.write(res.text)

	print('consume time :{}'.format((timeit.default_timer() - start)))



async def async_download(i):
	# async def는 해당 함수를 코루틴으로 만들어줍니다.
	# i: int 라는 부분은 type annotation입니다. 본 소스의 동작에는 일체의 영향을 주지 않습니다.
	async with aiohttp.ClientSession() as session: # requests의 Session 클래스 같은 역할입니다.
	    # 실제 요청을 비동기적으로 발생시킵니다.
		async with session.get(f'http://www.randomtext.me/api/lorem/p-1/32') as resp:
			# Python의 기본 open 함수는 비동기 입출력을 지원하지 않습니다. 그렇기에 외부 의존성을 씁니다.
            # 파일명 부분의 f'{i}.txt' 는 formatted string 구문입니다.
			async with aiofiles.open(f'{i}.txt', 'w') as f:
				await f.write(await resp.text())  # 결과를 text로 불러와서 파일에 저장합니다.


	

if __name__ == '__main__':
	# sync_download( 'sync' )

	makedir("async")
	os.chdir("async")
	start = timeit.default_timer()

	# 요청 2048개를 준비합니다.
	# 만든 당시에는 아직 아무것도 일어나지 않고, 아랫줄의 asyncio.wait에 의해 동시에 실행됩니다.
	tasks = [ async_download(x) for x in range(128) ]
	asyncio.run(asyncio.wait(tasks))
	print('consume time :{}'.format((timeit.default_timer() - start)))





