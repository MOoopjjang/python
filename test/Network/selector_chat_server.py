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
		socket = socket.socket()
		socket.bind((host , port))
		socket.listen(LISTEN_COUNT)
		socket.setblocking(False)
		return socket


	def _accepthandler_(self , srv_sock , mask ):
		cli_sock , cli_addr = srv_sock.accept()
		cli_sock.setblocking(False)
		print('connect : {}'.format(cli_addr))
		self._selectors.register(cli_sock , selectors.EVENT_READ , self._readhandler_)


	def _readhandler_(self , cli_sock , mask ):
		while True:
			read_msg = cli_sock.recv(1024)
			print('recv msg : {}'.format(read_msg.decode()))
			if read_msg.decode() == 'q':
				break

			cli_sock.sendall(read_msg)

		self._selectors.unregister(cli_sock)
		cli_sock.close()




	def run( self ):
		while True:
			events = self._selectors.select()
			for key , mask in events:
				callback = key.data
				callback( key.fileobj , mask )

