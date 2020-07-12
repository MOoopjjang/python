#!python3
# -*- coding:utf-8 -*-

import json
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world'

'''
 - rest api
'''
@app.route('/hello/<user>')
def hello_name(user):
    value_list = ['xferlog', 'kknda', 'bhkim']
    return render_template('hello.html', name=user, l=value_list)


'''
 - post 테스트
'''
@app.route('/auth/loginproc',methods=['POST'])
def loginproc():
    params = json.loads(request.get_data() , encoding='utf-8')
    email = params['email']
    pwd = params['pwd']
    print('email : {} , pwd : {}'.format(email , pwd))

    if email == 'cwkim@aaa.com' and pwd == '1111':
        return jsonify({'result':'OK'})
    else:
        return jsonify({'result':'FAILED'})

'''
 - rest api
 - get method
'''
@app.route('/person')
def person_info():
    _name = request.args.get('name')
    _age = request.args.get('age')
    data = {'name': _name, 'age': _age}
    return jsonify(data)



@app.route('/hello_html')
def hello_html():
    return render_template('hello.html')

@app.route('/auth/login')
def login():
    return render_template('login.html')








if __name__ == '__main__':
    app.run(host='localhost', port='8080', debug=True)



