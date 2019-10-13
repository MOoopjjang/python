#!python3
#-*- coding:utf-8 -*-


import socketserver

HOST , PORT = '0.0.0.0' , 5000



def f():
	return 'data'

class TestTCPHandler( socketserver.BaseRequestHandler ):
	def setup( self ):
		self.a = f()


	def handle( self ):
		print('handle')
		print('a : {}'.format(self.a))



class TestTCPServer( socketserver.TCPServer ):
	def __init__( self , serverAddress , handler ):
		socketserver.TCPServer.__init__(self , serverAddress , handler)



def test_1():
	tcpServer = TestTCPServer((HOST , PORT) , TestTCPHandler)
	tcpServer.serve_forever()





"""
	하나의 client 연결만 허용된다.
"""
#################################################################################
class MyTCPHandler( socketserver.BaseRequestHandler ):
	def handle( self ):
		while True:
			print('server hanle --------------')
			self.data = self.request.recv( 1024 ).strip()
			print( '{} wrote :'.format(self.client_address[0]))
			print( self.data.decode() )

			self.request.sendall( self.data.upper())

def normal():
	with socketserver.TCPServer((HOST , PORT) , MyTCPHandler) as server:
		server.serve_forever()

#################################################################################




"""
	Multi Client 지원
"""
#################################################################################
import threading
import time

class ThreadedTCPRequestHandler( socketserver.BaseRequestHandler ):
	def handle( self ):
		while True:
			self.data = self.request.recv( 1024 ).strip()
			current_thread = threading.current_thread()
			print('{} -- recv data : {}'.format(current_thread.name , self.data.decode()))

			print('send thread : {}'.format(current_thread.name))
			self.request.sendall(self.data)


class ThreadedTCPServer( socketserver.ThreadingMixIn , socketserver.TCPServer ):pass



def multiClient():
	server = ThreadedTCPServer( (HOST , PORT) , ThreadedTCPRequestHandler)
	with server:
		ip , port = server.server_address

		server_threading = threading.Thread(target = server.serve_forever )
		server_threading.daemon = True
		server_threading.start()
		print(' Server Loop running is thread : {}'.format(server_threading.name))

		server.serve_forever()


#################################################################################

import time
count = 1
def getData():
	global count
	count +=1

	# time.sleep(1)

	return str(count)+'\n'


class MTCPHandler( socketserver.BaseRequestHandler ):
	def setup( self ):
		self.systemInfo = getData()

	def handle( self ):
		while True:
			print('send data : {}'.format(self.systemInfo))
			self.request.sendall(self.systemInfo.encode())

			time.sleep(1)


		self.request.close()



class MTCPServer( socketserver.ThreadingMixIn , socketserver.TCPServer ):pass



def MServer_tst():
	mserver = MTCPServer((HOST , PORT) , MTCPHandler)
	with mserver:

		threading_server = threading.Thread(target = mserver.serve_forever)
		threading_server.daemon = True
		threading_server.start()

		mserver.serve_forever()





if __name__ == '__main__':
	# normal()

	# multiClient()

	# test_1()


	MServer_tst()





