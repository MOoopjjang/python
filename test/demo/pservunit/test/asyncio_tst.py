#!python3

'''
 - Non-blocking 연동 테스트
'''
import os,sys
import asyncio

T_HOST_1 = 'http://localhost:8080'


# def toJson(_text):
#     import json
#     return json.loads(_text)
async def fmsInteractionT1(_idx):
    import requests
    t_url = '/'.join([T_HOST_1 , 'file/info/dtl' , str(_idx)])
    return requests.get(t_url)



async def t1():
    import asyncio
    sys.path.append(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    )

    from util import str_util

    # from pservunit.util.str_util import toJson

    print(f'before')
    task = asyncio.create_task(fmsInteractionT1(1))
    print(f'after')
    await task
    return task.result().content


if __name__ == '__main__':
    # asyncio.run(t1())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(t1())
    loop.close()


