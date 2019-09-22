#!python3
#-*- coding:utf-8 -*-



import psutil



def tst_3():
	import uuid

	print(hex(uuid.getnode()))

	print('The MAC Address in formatted was is :',end='')
	mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0,8*6,8)][::-1])
	print(mac_address)

	





def tst_2():
	net_info = psutil.net_io_counters(pernic = True)
	print('net_info : {}'.format(net_info))



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
	# tst_1()

	# tst_2()

	tst_3()





