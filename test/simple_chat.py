#!python3
#-*- coding:utf-8 -*-


import socket
import sys , os




def main():
	chat_sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
	chat_host = socket.gethostname()
	chat_port = 12345 

	try:
		chat_sock.bind((chat_host , chat_port))
		chat_sock.listen(0)
		sid , addr = chat_sock.accept()
		while True:		
			# sid , addr = chat_sock.accept()
			print('connection from {}'.format(addr))
			msg = input('>>')
			sid.send(msg.encode())
			rcvmsg = sid.recv(1024).decode()
			if rcvmsg == 'disconnect':
				sid , addr = chat_sock.accept()
			print('<<{}'.format(rcvmsg))

	except:
		chat_sock.close()



if __name__ == '__main__':
	main()