#!python3
#-*- coding:utf-8 -*-


import socket
import threading

"""
mini chating client
"""

def server_chat(svc):
	while True:
		print('----------------')
		msgg = svc.recv(1024)
		print(msgg.decode())

if __name__ == '__main__':
	with socket.socket() as sc:
		sc.connect(('0.0.0.0' , 5000))

		t = threading.Thread(target = server_chat , args = (sc,))
		t.daemon = True
		t.start()
		while True:
			inputStr = input('>')
			sc.sendall(inputStr.encode())

		
		sc.close()
