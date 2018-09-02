#!python3
#coding:utf-8


import zipfile
import os


class MZip:
	def __init__( self ):
		pass

	@staticmethod
	def compress( dList , zfile ):
		"""
		file 이나 directory를 압축하는 method
		"""
		if len(dList) == 0:
			raise Exception('목록이 없습니다.')
		else:
			for l in dList:
				print('l >> %s'%l)
				pdir,fname = os.path.split(l.strip())
				if zfile == l.strip():
					os.chdir(pdir)
					print('compress ...  %s'%(l.strip()))
					if os.path.isfile(l.strip()):
						zObj = zipfile.ZipFile(fname+'.zip' , 'w')
						zObj.write(l.strip() , compress_type = zipfile.ZIP_DEFLATED )
						zObj.close()
					else:
						for d,s,filenames in os.walk(l.strip()):
							for fn in filenames:
								fullPath = os.path.join(d , fn)
								zObj = zipfile.ZipFile(fname+'.zip' , 'a')
								zObj.write(fullPath , compress_type = zipfile.ZIP_DEFLATED )
								zObj.close()


	@staticmethod
	def uncompress( compress_file ):
		"""
		압축된 file or directory를 해제 한다.
		"""
		zObj = zipfile.ZipFile( compress_file )
		zObj.extractall()
		zObj.close()
		


	@staticmethod
	def compressInfo( compress_file ):
		"""
		압축된 파일의 내부 파일들을 반환한다.
		"""
		zObj = zipfile.ZipFile( compress_file )
		return zObj.namelist()



if __name__ == '__main__':
	path = '/Users/MOoop/Documents/work/my/python/test/tt/sample_c.txt'
	MZip.compress([path] , path)

	path_z = '/Users/MOoop/Documents/work/my/python/test/tt/sample_c.txt.zip'
	print('{}'.format(MZip.compressInfo(path_z)))

	
	MZip.uncompress(path_z)









