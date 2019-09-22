#!python3
#-*- coding:utf-8 -*-


import socket


if __name__ == '__main__':
	with socket.socket() as sc:
		sc.connect(('0.0.0.0' , 5000))
		while True:
			print('----------------')
			# msg = input('>')
			# sc.sendall(msg.encode())
			msgg = sc.recv(1024)
			print(msgg.decode())

		sc.close()
