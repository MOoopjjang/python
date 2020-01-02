#!python3
#-*- coding:utf-8 -*-


import socket
import selectors


SERVER_ADDRESS = ('0.0.0.0' , 5000)
RECV_SIZE = 1024


client_socks = []

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

		client_socks.append(csock)

		self.selector.register( csock , selectors.EVENT_READ , self._readHandler)


	def _readHandler( self ,  cli_sock , mask ):
		msg = cli_sock.recv(RECV_SIZE)
		if msg:
			print('size : {}'.format(len(client_socks)))
			for cs in client_socks:
				msg_text = self.logmsg.format(server = self.__class__.__name__ , clinet = '' , rmsg = msg.decode())
				print(msg_text)
				cs.sendall(msg)
		else:
			self.selector.unregister( cli_sock )
			cli_sock.close()




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

