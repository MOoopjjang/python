#!python3
#-*- coding:utf-8 -*-


import cotyledon
import time
import socket
import threading
import logging
import subprocess


"""
  ----   Port Scanner ----

  기술 :
    - cotyledon ( processor 관리 module )
    - subprocess ( 다른 프로그램 실행 기능 )
    - socket을 통한 port scan기능
    - port를 통한 연결 process 정보 가져오기


  기능 :
   - open된 port와 연결된 program 이름
   - port + process name을 log로 출력
   - log를 화면에 process로 출력

"""


class PortScanner( cotyledon.Service ):
	def __init__( self , worker_id , conf_path ):
		super( PortScanner , self ).__init__( worker_id )
		self._shutdown = threading.Event()
		self._config = ConfigParser( conf_path )


	def __getResultFile( self , targetIp ):
		"""
		open된 port를 log로 저장
		"""
		from datetime import datetime
		fw = open(self._config.get('log') , 'a')
		fw.write('---'*10+targetIp+'<<>>'+str(datetime.now())+'---'*10+'\n')
		return fw




	def run( self ):
		while self._shutdown.is_set() != True:
			serverIp = socket.gethostbyname(self._config.get('host'))
			print('ip : {}'.format(serverIp))
			fw = self.__getResultFile(serverIp)
			for port in range(self._config.get('scan_start') , self._config.get('scan_end')):
				sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
				ret = sock.connect_ex((serverIp , port))
				if ret == 0:
					fw.write('Open Port : {} \n'.format(port))
					print('Open Port : {}'.format(port))
				sock.close()
			fw.close()

			# open된 port목록을 txt연결 프로그램을 이용하여 출력
			subprocess.Popen(['open' , self._config.get('log')])
			sleepTime = self._config.get('interval') * 60
			time.sleep(sleepTime)




	def terminate( self ):
		self._shutdown.set()



class ConfigParser:
	def __init__( self , path ):
		self.path = path
		self.jObj = None
		self._load()

	def __str__( self ):
		rl = [ k+'='+str(v) for k,v in self.jObj.items()]
		return ','.join(rl)


	def _load( self ):
		import json
		with open(self.path , 'r') as fr:
			self.jObj = json.load(fr)

	def get(self , attr):
		return self.jObj[attr]


		
def main():
	manager = cotyledon.ServiceManager()
	manager.add(PortScanner , 1 , ('config.json',))
	manager.run()


if __name__ == '__main__':
	main()







