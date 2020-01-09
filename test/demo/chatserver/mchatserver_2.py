#!python3
#-*- coding:utf-8 -*-



import select
import socket


SERVER_ADDRESS = ('0.0.0.0' , 9999)
ACCESS_COUNT = 100
MSG_BUFFER = 2048

'''

'''


class ChatSever2:

	SOCKET_HANDLER = {}

	def __init__( self ):
		self.SOCKET_LIST = []
		self.serv_sock = self._createServer()
		self.SOCKET_LIST.append(self.serv_sock)

		self.read_of_socks , self.write_of_socks , self.error = select.select(self.SOCKET_LIST , [] , [])

		SOCKET_HANDLER['srv_sock'] = self._handleServer
		SOCKET_HANDLER['cli_sock'] = self._handleCli




	def _handleServer( self , srv_sock ):
		csock , addr = srv_sock.accept()
		self.SOCKET_LIST.append(csock)




	def _handleCli( self , cli_sock ):
		msg = cli_sock.recv(MSG_BUFFER)
		if msg:
			try:
				self._broadcastMessage(msg)
			except:
				self.SOCKET_LIST.remove(cli_sock)
		else:
			self.SOCKET_LIST.remove(cli_sock)


	def _createServer( self ):
		serv_sock = socket.socket();
		serv_sock.bind(SERVER_ADDRESS)
		serv_sock.listen(ACCESS_COUNT)
		return serv_sock

	def run( self ):
		while True:
			for rsock in self.read_of_socks:
				cur_sock_key = 'srv_sock' if rsock == self.serv_sock else 'cli_sock'
				ChatSever2.SOCKET_HANDLER[cur_sock_key]()




	def _broadcastMessage( self , message ):pass





if __name__ == '__main__':
	pass
