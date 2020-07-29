#!python3
# -*- coding:utf-8 -*-


import asyncio
import websockets



async def accept(ws , path):
    while True:
        #receiving the data from client
        data_rcv = await ws.recv()
        print('received data = {}'.format(data_rcv))

        # send received data
        await ws.send('websock_svr send data = {}'.format(data_rcv))



if __name__ == '__main__':
    # websocket server create
    ws_server = websockets.serve(accept , 'localhost',3000)

    #waiting
    asyncio.get_event_loop().run_until_complete(ws_server)
    asyncio.get_event_loop().run_forever()
