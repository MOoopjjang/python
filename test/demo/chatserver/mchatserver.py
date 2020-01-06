#!python3
#-*- coding:utf-8 -*-


import socket
import selectors


SERVER_ADDRESS = ('0.0.0.0' , 5000)
RECV_SIZE = 1024


CLIENT_SOCKS = []

class MChatServer:
	def __init__( self ):
		self.selector = selectors.DefaultSelector()
		self._createSocket()
		## selector에 등록 ##
		self.selector.register( self.ssock , selectors.EVENT_READ , self._acceptHandler )
		self.logmsg = '{server} << {clinet} :: {rmsg} receive'


	def _createSocket( self ):
		'''
		 서버 socket을 생성한다
		'''
		self.ssock = socket.socket()
		self.ssock.bind(SERVER_ADDRESS)
		self.ssock.listen(100)
		## Non blocking mode ##
		self.ssock.setblocking( False )



	def _acceptHandler( self , server_sock , mask ):
		'''
			- server socket을 accept()호출
			- 전달받은 cli sock을 selectors에 등록
			- 반드시 nont blocking을 설정해야 된다.
		'''
		global client_socks

		csock , addr = server_sock.accept()
		csock.setblocking( False )
		self.selector.register( csock , selectors.EVENT_READ , self._readHandler)

		# server에 접속한 client socket을 list에 저장한다.
		CLIENT_SOCKS.append(csock)

		connectionMessage = '{} 님이 chatting방에 접속하셨습니다.\n'.format(addr)
		self._broadcastMessage(csock , connectionMessage.encode())

	def _readHandler( self ,  cli_sock , mask ):
		msg = cli_sock.recv(RECV_SIZE)
		if msg:
			print('connection client count : {}'.format(len(CLIENT_SOCKS)))
			self._broadcastMessage(cli_sock , msg)


		else:
			self.selector.unregister( cli_sock )
			cli_sock.close()
			CLIENT_SOCKS.remove(cli_sock)




	def _broadcastMessage(self , cli_sock  , message ):
		'''
		수신된 message를 접속한 client들에게 전송한다
		'''
		for cs in CLIENT_SOCKS:
			# 글을쓴 client에게는 메세지를 발송하지 않는다.
			if cs != cli_sock:
				# msg_text = self.logmsg.format(server = self.__class__.__name__ , clinet = cs , rmsg = message.decode())
				# print(msg_text)
				cs.sendall(message)





	def run( self ):
		'''
		event 루프를 돈다 
		'''
		while True:
			events = self.selector.select()
			for key , mask in events:
				callback = key.data
				callback( key.fileobj , mask)



if __name__ == '__main__':
	chatserver = MChatServer()
	chatserver.run()

