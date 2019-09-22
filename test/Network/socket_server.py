#!python3
#-*- coding:utf-8 -*-


import socket



if __name__ == '__main__':
	with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as sc:
		sc.bind(('0.0.0.0' , 5000))
		sc.listen(1)
		conn , addr = sc.accept()
		while True:
			msg = conn.recv(1024)
			print('echo : {}'.format(msg.decode()))
			conn.sendall(msg)


		sc.close()