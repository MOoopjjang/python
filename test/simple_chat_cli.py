#!python3
#-*- coding:utf-8 -*-


import sys , os
import socket




def main():
	chat_cli_sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
	server_host = socket.gethostname()
	port = 12345

	try:
		chat_cli_sock.connect((server_host , port))
		
		while True:
			resStr = chat_cli_sock.recv(1024).decode()
			print('<<{}'.format(resStr))
			if resStr == 'quit':
				chat_cli_sock.sendall('disconnect'.encode())
				chat_cli_sock.close()
				sys.exit(0)


			msg = input('>>')
			chat_cli_sock.sendall(msg.encode())

	except:
		chat_cli_sock.close()


if __name__ == '__main__':
	main()