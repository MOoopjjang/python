#!python
#-*- coding:utf-8 -*-


import mylog
import os , sys
import ConfigParser
import time


def parserConfig():
	config = ConfigParser.ConfigParser()
	config.read('monitoring.conf')
	f_items = dict(config.items('FILE'))
	s_items = dict(config.items('SEARCH'))

	return (f_items , s_items)


def getFileToBuffer( log_file ):
	fr = open(log_file , 'r')
	logData = fr.read()
	fr.close()
	return logData



def alert():
	print('Warning!!!')


def searching( search_word , index , logData ):
	nxt = logData.find( search_word  , index+1 , len(logData))	
	isFind = True
	if nxt == -1:
		index=len(logData)
		isFind = False
	else:
		index = nxt

	return (index , isFind)


def monitoring( f_items , s_items ):
	print(s_items.keys())
	b_line = int(s_items['beforeline'])
	a_line = int(s_items['afterline'])
	search_word = s_items['searchword']

	logData = getFileToBuffer(f_items['filepath'])
	index = logData.find( search_word )
	isFind = True
	if index == -1:
		isFind = False
		index = len(logData)
	else:
		isFind = True

	while True:
		if isFind:
			while True:
				alert()
				result = mylog.get_log_data( logData , index , b_line , a_line )
				print('{}'.format(result))
				(index , isFind) = searching( search_word  , index , logData)
				if isFind == False:break

		time.sleep(10)
		logData = getFileToBuffer(f_items['filepath'])
		(index , isFind) = searching( search_word  , index , logData)


def main():
	(f_items , s_items) = parserConfig()
	monitoring( f_items , s_items )



if __name__ == '__main__':
	main()