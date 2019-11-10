#!python3
#-*- coding:utf-8 -*-



import selectors
import socket


SERVER_HOST = '0.0.0.0'
SERVER_PORT = 5000
LISTEN_COUNT = 100

class ChatServer:
	def __init__( self ):
		self._selectors = selectors.DefaultSelector()
		self._socket = self._makesocket_(SERVER_HOST , SERVER_PORT)
		self._selectors.register(self._socket , selectors.EVENT_READ , self._accepthandler_)


	def _makesocket_( self , host , port ):
		s = socket.socket()
		s.bind((host , port))
		s.listen(LISTEN_COUNT)
		s.setblocking(False)
		return s


	def _accepthandler_(self , srv_sock , mask ):
		cli_sock , cli_addr = srv_sock.accept()
		cli_sock.setblocking(False)
		print('connect : {}'.format(cli_addr))
		self._selectors.register(cli_sock , selectors.EVENT_READ , self._readhandler_)


	def _readhandler_(self , cli_sock , mask ):
		read_msg = cli_sock.recv(1024)
		if read_msg:
			print('read_msg : {}'.format(read_msg.decode()))
			cli_sock.sendall(read_msg)
		else:
			self._selectors.unregister(cli_sock)
			cli_sock.close()




	def run( self ):
		while True:
			"""
			blocking -- 등록된 stream으로부터 EVENT_READ가 발생할때까지 대기
			"""
			events = self._selectors.select()
			for key , mask in events:
				callback = key.data
				callback( key.fileobj , mask )



if __name__ == '__main__':
	chat_server = ChatServer()
	chat_server.run()








