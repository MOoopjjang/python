#!python3
#-*- coding:utf-8 -*-


import os , sys


class MCleaner:
	def __init__( self  , _rootPath , _exts = None):
		self._rootPath = _rootPath
		self._exts = _exts


	def _contain_( self , ext ):
		for e in self._exts:
			if e == ext:return True

		return False


	def run( self ):
		print('*'*20)
		for d,s,fs in os.walk(self._rootPath):
			print('d : {}'.format(d))

			# for sd in s:
			# 	print('s : {}'.format(sd))

			for f in fs:
				fullPath = os.path.join(d,f)
				ss = f.split('.')
				if ss != None and len(ss) > 0:
					if self._contain_(ss[len(ss)-1]):
						print('delete : {}'.format(fullPath))
	

				# print('fullPath : {}'.format(fullPath))

		print('*'*20)




if __name__ == '__main__':
	mc = MCleaner('/Users/mooopjjang/Documents/work/Repository/bitbucket/python/msms' , ['sh'])
	mc.run()


