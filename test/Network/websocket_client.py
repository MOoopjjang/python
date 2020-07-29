#!python3
# -*- coding:utf-8 -*-

import asyncio
import websockets

async def mconnect():
    async with websockets.connect('ws://localhost:3000') as ws:
        for i in range(100):
            await ws.send('Hi server.i"m client -- {}'.format(i))
            data_rcv = await ws.recv()
            print('{} - recv_data : {}'.format(__file__ , data_rcv))




if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(mconnect())