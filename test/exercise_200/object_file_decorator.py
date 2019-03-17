#!python
#-*- coding:utf-8 -*-



def ObjectFileWriteDecorator( filePath=''  , enable = False):
	def Wrapped( inst ):
		def onDecorator(*args , **kargs ):
			if enable:
				import json
				import os
				ob = inst( *args , **kargs )
				if isinstance( inst , dict ) or len(inst.__dict__.keys()) == 0:
					raise Exception('Not Instance Error!!!')

				with open(filePath , 'a') as fw:
					strJson = json.dumps( ob.__dict__ )
					fw.write(strJson+'\n')
			return ob
		return onDecorator
	return Wrapped




def ObjectFileReadDecorator(filePath = '' , enable = False ):pass
