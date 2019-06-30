#!python3
#-*- coding:utf-8 -*-


import smtplib


def main():
	smtpObj = smtplib.SMTP('smtp.gmail.com' , 587)
	print(type(smtpObj))
	res = smtpObj.ehlo()
	print(res)

	res = smtpObj.starttls()
	print(res)

	res = smtpObj.login('MOoopjjang@gmail.com' , 'wpswkd1gkf')
	print(res)



if __name__ == '__main__':
	main()