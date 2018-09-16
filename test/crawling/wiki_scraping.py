#!python3
#-*- coding:utf-8 -*-


# Make by MOoop
# Desc
#	wiki page에서 제목과 첫번째 edit link를 수집하는 scraper



import bs4
from urllib.request import urlopen
import re
import logging
import string
import operator


def cleanInput( input ):
	input = re.sub('\n+',' ',input ).lower()
	# print('>>{}'.format(input))
	input = re.sub('\[[0-9]*\]' , '',input )
	input = bytes( input , 'UTF-8')
	input = input.decode('ascii' , 'ignore')
	cleanInput = []
	input = input.split(' ')
	for item in input:
		item = item.strip(string.punctuation)
		if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
			cleanInput.append( item )

	print('len >> {}'.format(len(cleanInput)))
	return cleanInput


def ngrams( input , n ):
	input = cleanInput( input )
	output = {}
	for i in range( len(input)-n+1 ):
		# ngramTemp = ' '.join(input[i:i+n])
		ngramTemp = ' '.join(input[i:i+n])
		if ngramTemp not in output:
			output[ ngramTemp ] = 0
		output[ngramTemp] +=1
	return output


def main():
	content = str(urlopen('http://pythonscraping.com/files/inaugurationSpeech.txt').read() , 'utf-8')
	ng = ngrams(content , 2)
	sortedNGrams = sorted(ng.items() , key = operator.itemgetter(1) , reverse = True)
	print(sortedNGrams)



	



if __name__ == '__main__':
	main()