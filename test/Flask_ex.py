#!python
# -*- coding:utf-8 -*-


from flask import Flask , request

app = Flask(__name__)

app.debug = True

# @app.route("/")
@app.route("/hello")

# def hello():
# 	return "Hello World"

def hello_to(param):
	n = request.args.get('name')
	return 'hello , {}'.format(n)

if __name__ == '__main__':
	app.run()