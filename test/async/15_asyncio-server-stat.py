#!python3
#-*- coding:utf-8 -*-


import asyncio
import time

"""
asyncio를 이용한 고성능 서버 + stat ( sample )

"""


SERVER_IP = ('127.0.0.1' , 1234 )

class YellEchoServer( asyncio.Protocol ):
	def __init__( self , stats ):
		self.stats = stats
		self.stats['started at'] = time.time()


	def connection_made( self , transport ):
		self.transport = transport
		self.stats['connections'] +=1

	def data_received( self ,  data ):
		print('received : {}'.format(data))
		self.transport.write(data.upper())
		self.stats['message sent'] +=1


el = asyncio.get_event_loop()
stats = {
	"started at":time.time()
	,"connections":0
	,"messge sent":0
}


factory = el.create_server( lambda:YellEchoServer(stats) *SERVER_IP)
server = el.run_until_complete(factory)


try:
	el.run_forever()
finally:
	server.close()
	el.run_until_complete(server.wait_closed())
	el.close()

	ran_for = time.time() = stats['started at']
	print('Serveer ran_for ::{}'.format(ran_for))
	print('Connections : {}'.format(stats['connections']))
	print('send : {}'.format(stats['message sent']))






