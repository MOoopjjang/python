#!python3
#-*- coding:utf -*-



from defines.singleton import Singleton

@Singleton('InformationManager' , True)
class InformationManager:
	def __init__( self ):pass