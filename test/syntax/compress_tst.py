#!python3
#-*- coding:utf-8 -*-

'''
- 압축 module 테스트
- zipfile
- bzip , gzip
'''

import os
import zipfile


def zipfile_password():
	td = os.path.join(os.getcwd() , 'ziptest' , 'sample.zip')
	nSelect = int(input('1.compress 2.extract >>'))
	if nSelect == 1:
		l = ['tst1.py' , 'tst2.py']
		if os.path.exists(td):
			os.unlink(td)

		with zipfile.ZipFile(td ,compresslevel = 9, mode = 'w') as nw:
			nw.setpassword('1111'.encode())
			for fn in l:
				nw.write(fn , compress_type=zipfile.ZIP_DEFLATED )
	else:
		with zipfile.ZipFile(td) as zf:
			print('list : {}'.format(zf.namelist()))
			os.mkdir(os.path.join(os.getcwd() , 'ziptest' , 'sample'))
			zf.extractall(os.path.join(os.getcwd() , 'ziptest' , 'sample'))



def zipfile_compress_info():
	td = os.path.join(os.getcwd() , 'ziptest' , 'sample.zip')
	with zipfile.ZipFile(td) as zi:
		print('list : {}'.format(zi.namelist()))
		print('arch info : {}'.format(zi.infolist()))

		tst1Info = zi.getinfo('tst1.py')
		print('file size : {}'.format(tst1Info.file_size))
		print('compress size : {}'.format(tst1Info.compress_size))


def zipfile_compress_tst1():
	td = os.path.join(os.getcwd() , 'ziptest' , 'sample.zip')
	with zipfile.ZipFile(td) as ne:
		ne.extract('tst1.py' , os.path.join(os.getcwd() , 'ziptest' , 'sample'))


def zipfile_compress_tst():

	td = os.path.join(os.getcwd() , 'ziptest' , 'sample.zip')
	nSelect = int(input('input 1.compress 2.extract >> '))
	if nSelect == 1:
		l = ['tst1.py' , 'tst2.py']
		
		if os.path.exists(td):
			os.unlink(td)

		print('td : {}'.format(td))
		with zipfile.ZipFile(td , 'w') as nz:
			for f in l:
				nz.write(f , compress_type=zipfile.ZIP_DEFLATED )
	else:
		with zipfile.ZipFile(td) as zf:
			print('list : {}'.format(zf.namelist()))
			os.mkdir(os.path.join(os.getcwd() , 'ziptest' , 'sample'))
			zf.extractall(os.path.join(os.getcwd() , 'ziptest' , 'sample'))


	print('end')


	
	# newzip = zipfile.ZipFile('./')


	



if __name__ == '__main__':
	# zipfile_compress_tst()
	# zipfile_compress_tst1()
	# zipfile_compress_info()

	zipfile_password()




