#!python3
#-*- coding:utf-8 -*-


# Make by MOoop
# Desc:
#    Multi Web Crawler..릿(image)


# History
# v0.6.0
#	>>> create
# v0.7.0
#	>>> Zip 옵션추가 (-z) , MultiProecess 옵션추가 (-m)
# v0.7.1
#	>>> OptionParser 기능 추가
# v0.8.0
#	>>> Download시 병렬 다운로드 기능 지원 (Multi Processing)


import bs4
import requests
import sys
import os
import mcrawler
from mglobal import init , getLogger , getCurrentTime , getDefCurrentTime
from optparse import OptionParser

d = {}

def getZipOption():
	global parser
	(options , args) = parser.parse_args()
	return options.zip


def getMPOption():
	global parser
	(options , args) = parser.parse_args()
	if options.mp == False:
		return 0
	else:
		return int(options.mp)

def getMaxDepth():	
	global parser
	(options , args) = parser.parse_args()
	if options.depth == False:
		return 0
	else:
		return int(options.depth)



def getOption():
	global parser
	usage = """ %prog [propertie file] [option]
	ex) %prog wc.propertis 
	ex) %prog wc.propertis -m [0,2,4,6,8,10] -z -d [0-3]
	"""

	parser = OptionParser(usage = usage)
	parser.add_option('-z' , '--zip' , action = 'store_true' , help = 'Compress Download image file' , default = False)
	parser.add_option('-m' , '--MP' , dest = 'mp' , help = 'Multi Processing Downloading ...' , default = False)
	parser.add_option('-d' , '--Depth' , dest = 'depth' , help = 'Download Web Page Depth' , default = False)

	(options , args) = parser.parse_args()
	if len(args) == 0:
		parser.print_help()
		sys.exit(0)



def loadProperties():
	global d

	fread = open(sys.argv[1] , 'r')
	dir_list = []
	url_list = []
	for line in fread:
		if line.startswith('wc.dir') == True:
			_,sd = line.split(':::')
			if sd[-1] == '\n':
				sd = sd[0:-1]
			dir_list.append(sd)
		elif line.startswith('wc.url') == True:
			_,url = line.split(':::')
			if url[-1] == '\n':
				url = url[0:-1]
			url_list.append(url)

	d['dirs'] = dir_list
	d['urls'] = url_list



def main():
	init()
	getOption()
	loadProperties() 

	getLogger().debug(d['dirs'])
	getLogger().debug(d['urls'])
	getLogger().debug('mp : {} , z:{} , d:{}'.format(getMPOption() , getZipOption() , getMaxDepth()))

	getLogger().info('-- Crawling ... start ::{}'.format(getDefCurrentTime()))

	# RUN
	crawler = mcrawler.MCrawler(d['urls'] , d['dirs'] , getMPOption() , getZipOption(),getMaxDepth())
	crawler.run()

	getLogger().info('-- Crawling ... end ::{}'.format(getDefCurrentTime()))


if __name__ == '__main__':
	main()


