#!python
#coding:utf-8


# Maky by cwkim

# Desc:
#	- Redis to Redis 간에  copy , compare , delete 기능을 제공한다.

# 구현 필요사항 :
#	- Multi key  방식

# History
#	- 2018.05.03 	Create
#	- 2018.05.14 	OptionParser적용 , key단위 처리 (copy , 삭제 , compare )기능 추가
#	- 2018.05.15	Multi Key 기능 추가
# 
# version 0.9.0

import sys , os
import re
import mredisconfig
import mredismanager
from optparse import OptionParser
from mcommmodule import getLogger , getCurrentDefTime



def getOption():
	global parser

	usage = """ %prog [option]
	ex1) %prog -t [rtoc|rtor|rtorp] -m [copy|compare|delete] -k [key] -f [Field Key]
	"""

	parser = OptionParser(usage = usage)
	parser.add_option('-t' , '--type' , dest = 'type' , help = 'rtoc , rtor , rtorp' , default = None)
	parser.add_option('-m' , '--mode' , dest = 'mode' , help = 'copy , compare , delete' , default = None)
	parser.add_option('-k' , '--key' , dest = 'key' , help = 'Redis Key' , default = None)
	parser.add_option('-f' , '--fkey' , dest = 'fkey' , help = 'Field Key In HashMap' , default = None)


	(options , args) = parser.parse_args()
	getLogger().debug('args len ::{}'.format(len(args)))
	getLogger().debug('options  ::{}'.format(options.__str__))

	if options.type == None or options.mode == None:
		parser.print_help()
		sys.exit(0)


def main():

	getOption()
	(options , args) = parser.parse_args()

	conf = mredisconfig.MRedisConfig()
	rmgr = mredismanager.MRedisManager(conf)
	rmgr.setTypeMode(options.type , options.mode).setKey(options.key , options.fkey).run()


if __name__ == '__main__':
	main()

