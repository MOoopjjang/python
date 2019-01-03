#!python3
#-*- coding:utf-8 -*-


import asyncio

"""
asyncio를 이용한 고성능 서버 ( sample )

"""

SERVER_IP = ('127.0.0.1' , 1234 )

class YellEchoServer( asyncio.Protocol ):
	def connection_made( self , transport ):
		self.transport = transport
		print('Connection from receive:{}'.format(self.transport.get_extra_info('peername')))

	def data_received(self , data):
		print('recv : {}'.format(data))
		self.transport.write(data.upper())


	def connection_lost( self , exc ):
		print('Client disconnect!!!')


el = asyncio.get_event_loop()

factory = el.create_server( YellEchoServer , *SERVER_IP )
server = el.run_until_complete( factory )


try:
	el.run_forever()
finally:
	server.close()
	el.run_until_complete(server.wait_closed())
	el.close()

