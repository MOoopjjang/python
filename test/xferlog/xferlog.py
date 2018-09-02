
#coding:utf-8

class Test():
	jump = 1.1
	def __init__(self , name , age , pay):
		self.name = name
		self.age = age
		self.pay = pay


	def pay_raise(self):
		self.pay = self.pay * self.jump

	def info(self):
		return '{} 님의 나이는 {} 이며 , pay는 {} 이다'.format(self.name , self.age , self.pay)		