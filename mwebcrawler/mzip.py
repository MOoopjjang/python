#!python3
#coding:utf-8


import zipfile
import os
import logging


class MZip():
	def __init__(self):
		pass

	def __del__(self):
		pass	


	def fileCompress(_file):
		pass

	@staticmethod
	def dirCompress(_dir):
		
		_,zn = os.path.split(_dir)
		zf = zipfile.ZipFile(_dir+'/'+zn+'.zip' , 'w')
		for dn,sdn,fn in os.walk(_dir):
			zf.write(dn , compress_type = zipfile.ZIP_DEFLATED)
			print('Add Zip...'+dn)
			for fns in fn:
				if fns.endswith('.zip') == True:
					continue
				zf.write(os.path.join(dn , fns) , compress_type = zipfile.ZIP_DEFLATED)

		zf.close()



	@staticmethod
	def compress(org , _logging):
		if os.path.isfile(org) == True:
			MZip.fileCompress(org)
		else:
			MZip.dirCompress(org)





	# def compress(org1 , org2):
	# 	pass

