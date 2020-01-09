#!python3
#-*- coding:utf-8 -*-



import select
import socket


SERVER_ADDRESS = ('0.0.0.0' , 5000)
ACCESS_COUNT = 100
MSG_BUFFER = 2048

'''

'''


class ChatSever2:

	SOCKET_HANDLER = {}

	def __init__( self ):
		self.SOCKET_LIST = []
		self.srv_sock = self._createServerSocket()
		self.SOCKET_LIST.append(self.srv_sock)

		ChatSever2.SOCKET_HANDLER['srv_sock'] = self._handleServer
		ChatSever2.SOCKET_HANDLER['cli_sock'] = self._handleCli


	def _handleServer( self , srv_sock ):
		csock , addr = srv_sock.accept()
		self.SOCKET_LIST.append(csock)
		csock.setblocking(False)
		self._broadcastMessage(csock , '채팅방에 {} 님이 입장하셨습니다.\n'.format(addr))




	def _handleCli( self , cli_sock ):
		try:
			msg = cli_sock.recv(MSG_BUFFER)
		except ssl.SSLError as e:
			if e.errno != ssl.SSL_ERROR_WANT_READ: 
				raise

		
		if msg:
			try:
				self._broadcastMessage(cli_sock , msg)
			except:
				self.SOCKET_LIST.remove(cli_sock)
		else:
			self.SOCKET_LIST.remove(cli_sock)
			cli_sock.close()


	def _createServerSocket( self ):
		serv_sock = socket.socket();
		serv_sock.bind(SERVER_ADDRESS)
		serv_sock.listen(ACCESS_COUNT)
		return serv_sock


	def run( self ):
		while True:
			read_of_socks , write_of_socks , error = select.select(self.SOCKET_LIST , [] , [])
			for rsock in read_of_socks:
				cur_sock_key = 'srv_sock' if rsock == self.srv_sock else 'cli_sock'
				ChatSever2.SOCKET_HANDLER[cur_sock_key](rsock)


		self.srv_sock.close()




	def _broadcastMessage( self , cli_sock ,  message ):
		for csock in self.SOCKET_LIST:
			try:
				if csock != cli_sock and csock != self.srv_sock:
					csock.send(message)
			except:
				self.SOCKET_LIST.remove(cli_sock)
				csock.close()
				continue
			






if __name__ == '__main__':
	chatserver2 = ChatSever2()
	chatserver2.run()

	








