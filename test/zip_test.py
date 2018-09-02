#!python
#-*- coding:utf-8 -*-


import zipfile , os



def main():
	path = os.getcwd()+'/tt'
	print('curDir >> %s'%(path))
	_,zipname = os.path.split(path)
	zipname += '.zip'
	print('name >> %s'%zipname)
	zObj = None
	if os.path.isfile(path):
		zObj = zipfile.ZipFile(zipname , 'w')
		zObj.write(path , compress_type = zipfile.ZIP_DEFLATED )
		zObj.close()
	else:
		for d , s , filenames in os.walk(path):
			for f in filenames:
				fullPath = os.path.join(d,f)
				# inPath = fullPath[len(path)+1:]
				# print('f >> %s , %s'%(fullPath , inPath))

				zObj = zipfile.ZipFile(zipname , 'a')
				zObj.write(fullPath , compress_type = zipfile.ZIP_DEFLATED )
				zObj.close()


				


if __name__ == '__main__':
	main()