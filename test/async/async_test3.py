#!python3
# -*- coding:utf-8 -*-

import asyncio
import timeit



def tst_sync():
    def t1(n):
        import time
        for i in range(1, n + 1):
            print(f'{i} -- {n}명중')
            time.sleep(1)
        print(f'총 {n} 명 동기화 완료')

    s = timeit.default_timer()
    t1(3)
    t1(2)
    t1(1)
    print('총 소요시간 {}'.format(timeit.default_timer() - s))



async def tst_async():
    async def t(n):
        for i in range(1, n + 1):
            print(f'{i} -- {n}명중')
            await asyncio.sleep(1)
        print(f'총 {n} 명 동기화 완료')

    s = timeit.default_timer()
    await asyncio.wait([t(3) , t(2) , t(1)])

    print('총 소요시간 {}'.format(timeit.default_timer() - s))



if __name__ == '__main__':
     asyncio.run(tst_async())
    # tst_sync()



