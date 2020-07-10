#!python3
# -*- coding:utf-8 -*-


from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world'


@app.route('/hello/<user>')
def hello_name(user):
    value_list = ['xferlog', 'kknda', 'bhkim']
    return render_template('hello.html', name=user, l=value_list)


@app.route('/hello_html')
def hello_html():
    return render_template('hello.html')


@app.route('/person')
def person_info():
    _name = request.args.get('name')
    _age = request.args.get('age')
    data = {'name': _name, 'age': _age}
    return jsonify(data)


if __name__ == '__main__':
    app.run(host='localhost', port='8080', debug=True)
