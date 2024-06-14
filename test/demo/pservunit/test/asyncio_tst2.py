#!python
import asyncio
import timeit

T_HOST_1 = 'http://localhost:9080'

loop = asyncio.get_event_loop()

async def fmsInteractionT1(t_url):
    import requests
    return requests.get(t_url)



async def t2(_cnt):
    urls = [asyncio.create_task(fmsInteractionT1('/'.join([T_HOST_1, 'api/t2']))) for _ in
            range(_cnt)]
    results = await asyncio.gather(*urls)
    for url in urls:
        url.result()
    print(f'result = {len(results)}')


if __name__ == '__main__':
    start = timeit.default_timer()
    loop.run_until_complete(t2(3))
    loop.close()
    print(f'--- complete --- {timeit.default_timer() - start}')
