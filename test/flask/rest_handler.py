#!python3.8.1
#-*- coding:utf-8 -*-


from flask import Flask
from flask_restful import Api

from flask_restful import Resource
from flask_restful import reqparse



class Plus(Resource):
    def get(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('x',required = True , type = int , help='x cannot be blank')
            parser.add_argument('y',required = True , type = int , help='y cannot be blank')
            args = parser.parse_args()
            result = args['x'] + args['y']
            return {'result':result}
        except Exception as e:
            return {'error':str(e)}



if __name__ == '__main__':
    app = Flask('My First App')
    api = Api(app)
    api.add_resource(Plus , '/plus')

    app.run(host = '0.0.0.0',port = 8080 , debug = True)
