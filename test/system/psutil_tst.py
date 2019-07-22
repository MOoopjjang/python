#!python3
#-*- coding:utf-8 -*-



import psutil


def tst_1():

	# print(psutil.net_connections())
	for value in psutil.net_connections():
		try:
			if value.laddr != None and value.laddr[0] != '127.0.0.1' and (value.status == 'LISTEN' or value.status == 'ESTABLISHED'):
				print('{}:{} - {}:{} - {}'.format(value.pid , psutil.Process(value.pid).name() , value.laddr[0],value.laddr[1],value.status))

			# print("{}:{}".format(value.laddr[0],value.laddr[1]))
			# print(value.raddr)
			# print(value.pid)
			# print(psutil.Process(value.pid).name())
			# print(value.status)
			# break
		except:pass
		





if __name__ == '__main__':
	tst_1()