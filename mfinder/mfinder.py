#!python3
#coding:utf-8


# Make by:
#	MOoop
# Version
#	0.7.2
	


#
# History
# 	0.5.0 2018.04.20     
#   0.6.0 2018.04.20
#		>>>  Pattern Matching기능 추가
#	0.6.1 2018.04.22
#		>>> class로 분리
#   0.6.2 2018.04.29
#		>>> option값 추가 
#   0.7.0 2018.07.10
#		>>> 한글검색 bug수정
#   0.7.1 2018.07.27
#		>>> 검색결과 삭제기능 미동작 벼그 수정.
#   0.7.2 2018.08.01
#		>>> 소스 Refactoring.

import sys , os
import logging
import platform


import msearch
import mfilehandle
import mglobal
from optparse import OptionParser
import mzip


def getOption():
	global parser

	usage = """ %prog [ file path ] [ search text ] [ option ]
	ex) %prog /User/MOoop '*'
	ex) %prog / 'txt'
	ex) %prog /svc 'access*|mp4$'
	ex) %prog /svc '.txt' -s -n
	"""
	parser = OptionParser(usage = usage)
	parser.add_option('-s' , '--save' , action = 'store_true' , help = 'search_result.txt write search result' , default = False)
	parser.add_option('-n' , '--next' , action = 'store_true' , help = 'Next Step' , default = False)
	# parser.add_option('-d' , '--del' , action = 'store_true' , help = 'Delete Search result file')

	(options , args) = parser.parse_args()
	if len(args) < 2:
		parser.print_help()
		sys.exit(0)


def getSaveOption():
	global parser
	(options , args) = parser.parse_args()
	return options.save

def getAddOption():
	global parser
	(options , args) = parser.parse_args()
	return options.next

def main():
	mglobal.init()
	mglobal.setLogLevel('debug')
	getOption()

	mglobal.getLogger().debug('s : {} , n : {}'.format(getSaveOption() , getAddOption()))

	resultFile = None
	if getSaveOption() == True:
		resultFile = 'search_result.txt'
		if os.path.exists(os.getcwd()+'/'+resultFile) == True:
			os.unlink(os.getcwd()+'/'+resultFile)
		
	ms = msearch.Search(resultFile)
	ms.setSearchInfo(sys.argv[1] , sys.argv[2])
	ms.find()
	# ms.print()
	for p in ms:
		print('{}'.format(p))


	try:
		if getAddOption() == True:
			while True:
				num = input('1.delete\t2.zip\t3.zip and delete\t4.quit?')
				select = int(num)
				if select == 4:
					sys.exit(0)
				elif select == 1:
					filename = input('삭제할 파일이름을 입력하세요(파일이름만 입력하세요):')
					mfilehandle.MFileHandle.deleteFile(ms.getResultList() , filename)
				elif select == 2:
					filename = input('압축할 파일이름을 입력하세요(전체 경로):')
					mzip.MZip.compress(ms.getResultList() , filename)

	except:
		sys.exit(0)

	



if __name__ == '__main__':
	main()



