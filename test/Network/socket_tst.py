#!python3
#-*- coding:utf-8 -*-


import socket
import threading
import time



def server():
	# 1. socket을 생성
	with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as sc:
		print('listen.....')
		sc.bind(('0.0.0.0',5000))
		while True:
			sc.listen(1)
			conn , addr = sc.accept()
			msg = conn.recv(1024)
			print(f'{msg.decode()}')
			conn.sendall(msg)


		sc.close()



def client():
	with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as sc:
		sc.connect(('0.0.0.0' , 5000))
		while True:
			line = input('>')
			sc.sendall(line.encode())
			res = sc.recv(1024)
			print(f'{res.decode()}')
			






def main():

	s = threading.Thread(target = server)
	s.start()

	time.sleep(10)

	print('----------------------------')
	c = threading.Thread(target = client)
	c.start()










if __name__ == '__main__':
	main()




