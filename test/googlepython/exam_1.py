#!python3
#-*- coding:utf-8 -*-


#

import pymysql
import MAESClipher


SELECT_QUERY = 'select * from TBL_PY'


conn = None
cursor = None


def dbconnection():
	global conn
	global cursor

	conn = pymysql.connect(host = 'localhost' , user = 'MOoop' , passwd = '1111' , db = 'testdb' , charset='utf8')
	cursor = conn.cursor()


def testinsert():
	global conn
	global cursor

	data = (
			('xferlog' , '' , ''),
			('kknda' , '' , ''),
			('kthda' , '' , ''),
			('zinnawork' , '' , '')
		)

	for l in data:
		qry = 'insert into TESTDB.TBL_PY (ORG,ORGENC,ORGDEC) VALUES (%s , %s , %s)'
		cursor.execute(qry , l)
	conn.commit()


def update(_where , _enc , _dec):
	_enc = _enc.decode('utf-8')
	_dec = _dec.decode('utf-8')
	v = (_enc , _dec , _where)

	query = 'UPDATE TESTDB.TBL_PY SET ORGENC=%s,ORGDEC=%s WHERE ORG=%s'
	cursor.execute(query , v)
	conn.commit()

def select(_qry):
	global cursor
	cursor.execute(_qry)
	return cursor.fetchall()


def allDisplay():
	rs = select(SELECT_QUERY)
	for row in rs:
		print('o :{} , e:{} , d:{}'.format(row[0] , row[1] , row[2]))


def main():
	aesUtil = MAESClipher.MAESClipher('ABCDEFGHIK123456KL')
	dbconnection()


	rs = select(SELECT_QUERY)
	for row in rs:
		_e = aesUtil.encrypt(row[0])
		_d = aesUtil.decrypt(_e)
		update(row[0] , _e , _d)

	allDisplay()

	conn.close()


if __name__ == '__main__':
	main()

