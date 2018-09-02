#!python3
#-*- coding:utf-8 -*-


import base64
import hashlib

from Crypto import Random
from Crypto.Cipher import AES

class MAESClipher:
	BS = 16
	pad = lambda s: s + (MAESClipher.BS - len(s) % MAESClipher.BS) * chr(MAESClipher.BS - len(s) % MAESClipher.BS)
	unpad = lambda s : s[0:-s[-1]]

	def __init__(self , key):
		self.__key = hashlib.sha256(key.encode('utf-8')).digest()


	def encrypt(self , _data):
		_data = MAESClipher.pad(_data)
		iv = Random.new().read(AES.block_size)
		cipher = AES.new( self.__key, AES.MODE_CBC, iv)
		return base64.b64encode(iv + cipher.encrypt(_data))


	def decrypt(self , _enc):
		_enc = base64.b64decode( _enc )
		iv = _enc[:16]
		cipher = AES.new(self.__key , AES.MODE_CBC , iv)
		return MAESClipher.unpad(cipher.decrypt( _enc[16:] ))


if __name__ == '__main__':
	aes = MAESClipher('xferlogkknda')
	enc = aes.encrypt('01098113963')
	dec = aes.decrypt(enc)

	print('enc ::{}'.format(enc))
	print('dec :: {}'.format(dec))


