#!python3
#-*- coding:utf-8 -*-


import socket
import time



if __name__ == '__main__':
	with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as sc:
		sc.bind(('0.0.0.0' , 5000))
		sc.listen(1)
		conn , addr = sc.accept()
		data = 'xferlog'
		while True:
			# msg = conn.recv(1024)
			# print('echo : {}'.format(msg.decode()))
			conn.sendall('msg\n'.encode())
			time.sleep(1)



		sc.close()