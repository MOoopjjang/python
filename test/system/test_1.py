#!python3
#-*- coding:utf-8 -*-


import platform
import multiprocessing



def info():
	print('os >> {}'.format(platform.system()))
	print('os detail >> {}'.format(platform.platform()))
	print('os version >> {}'.format(platform.version()))
	print('processor >> {}'.format(platform.processor()))
	print('CPU count >> {}'.format(multiprocessing.cpu_count()))

	print('Mac : {}'.format(platform.mac_ver()))


def socket_module_sample():
	import socket
	host = socket.gethostbyname_ex('www.google.com')
	print('\n'+'-'*10+'Host info'+'-'*20)
	print('{}'.format(host))

	print('\n'+'-'*10+'Host info Line'+'-'*20)
	for i in host:
		print('{}'.format(i))

	(hostname , aliaslist , ipaddrlist ) = host
	print('\n'+'-'*10+'IP Address'+'-'*20)
	print('{}'.format(ipaddrlist[0]))



def connection():
	import os

	select = input('Connection server Y/N?')
	if select == 'Y':
		os.system('ssh svc@10.211.55.3')



def main():
	info()
	# socket_module_sample()
	# connection()


if __name__ == '__main__':
	main()