#!python3
#-*- coding:utf-8 -*-


import socket 
import time
import threading

"""
mini chatting server
"""

csocks = []
def client( csock , addr ):
	global csocks

	csock.sendall(('{} hi'.format(addr)).encode())
	while True:
		msg = csock.recv(5000)
		if msg.decode() == 'quit':
			break

		strAddr = str(addr[0])+':'+str(addr[1])
		notiMsg = strAddr+'>'+str(msg.decode())
		for sd in csocks:
			sd['sock'].sendall(notiMsg.encode())
			

def chat():
	global csocks

	with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as sc:
		sc.bind(('0.0.0.0' , 5000))
		sc.listen(5)
		while True:
			csock , addr = sc.accept()
			csocks.append({'sock':csock , 'addr':addr})
			csock_thread = threading.Thread(target = client , args = (csock , addr,))
			csock_thread.daemon = True
			csock_thread.start()

			





def normal():
	with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as sc:
		sc.bind(('0.0.0.0' , 5000))
		sc.listen(5)
		cs , addr = sc.accept()
		print('client addr : {}'.format(addr))
		cs.sendall('hi'.encode())
		r = cs.recv(5000)
		print('client->server : {}'.format(r.decode()))

		cs.close()





if __name__ == '__main__':
	# main()

	chat()
