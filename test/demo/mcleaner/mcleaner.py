#!python3
#-*- coding:utf-8 -*-


import os , sys
from progress.bar import PixelBar


class MCleaner:
	def __init__( self  , _rootPath  , _config):
		self._rootPath = _rootPath
		self._config = _config



	def _contain_( self , ext ):
		for e in self._config.get('exts'):
			if e == ext:return True

		return False


	def run( self ):
		print('*'*100)
		saveResultFile = None
		if self._config.get('result') == None or len(self._config.get('result').strip()) == 0:
			saveResultFile = os.path.join(os.getcwd() , 'result.txt') 
		else:
			saveResultFile = self._config.get('result')
		if os.path.exists(saveResultFile):os.unlink(saveResultFile)

		with PixelBar('Delete progressing...') as bar:
			with open(saveResultFile , 'w') as fw:
				count = 0
				for d,s,fs in os.walk(self._rootPath):
					for f in fs:
						fullPath = os.path.join(d,f)
						ss = f.split('.')
						if ss != None and len(ss) > 0:
							if self._contain_(ss[len(ss)-1]):
								os.unlink(fullPath)
								# print('delete : {}'.format(fullPath))
								fw.write(fullPath+'\n')
								count +=1

						bar.next()

	
		print('*'*100)
		print('root : {}'.format(self._rootPath))
		print('save : {}'.format(saveResultFile))
		print('delete count : {}'.format(count))
		print('-'*100)




if __name__ == '__main__':
	mc = MCleaner('/Users/mooopjjang/Documents/work' , ['pyc'])
	mc.run()


