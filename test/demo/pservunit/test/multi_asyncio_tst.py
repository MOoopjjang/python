#!python3

import asyncio
from concurrent.futures import ThreadPoolExecutor


async def api(_url , _method , _data , _headers):
    import requests
    eFunc = requests.get if _method=='GET' else requests.post
    return eFunc(_url , data = _data , headers = _headers)


def c_task(_func , *args):
    return asyncio.create_task(_func(*args))


async def c_job(_url , _method , _data , _headers):
    task = await c_task(api , _url , _method , _data , _headers)
    return task.content



def c_evntloop(_url, _method , _data , _headers):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    r = loop.run_until_complete(c_job( _url, _method , _data, _headers))
    loop.close()
    return r


def create_eventloop(_cnt , _url , _method , _data , _headers):
    with ThreadPoolExecutor(max_workers=_cnt+1) as executor:
        fs = [ executor.submit(c_evntloop , _url , _method , _data , _headers) for _ in range(_cnt) ]
        for f in fs:
            r = f.result()
            print(f'>>>r = {r}')

if __name__ == '__main__':
    create_eventloop(3 ,'http://localhost:9080/api/t2' , 'GET' , None , None )