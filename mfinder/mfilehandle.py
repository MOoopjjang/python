
#coding:utf-8


import os
import shutil



class MFileHandle:
	def __init__(self):
		pass

	@staticmethod
	def deleteFiles(dlist):
		if len(dlist) == 0:
			raise Exception('삭제할 파일목록이 없습니다')

		for l in dlist:
			if os.path.exists(l) == True:
				os.unlink()
				print('Delete ... '+l.strip())

	@staticmethod
	def deleteFile(dList , dfile):
		if len(dList) == 0:
			raise Exception('삭제할 파일목록이 없습니다')
		for l in dList:
			_,sfile = os.path.split(l.strip())
			if dfile == sfile:
				print('Delete .. '+l.strip())
				os.unlink(l.strip()) if os.path.isfile(l.strip()) else shutil.rmtree(l.strip())	
