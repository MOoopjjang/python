#!python3
# -*- coding:utf-8 -*-


from socketserver import BaseRequestHandler, UDPServer
import time

class TimeHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from' , self.client_address)
        # 클라이언트 소켓과 메시지 얻기
        msg , sock = self.request
        resp = time.ctime()
        sock.sendto(resp.encode('utf-8') , self.client_address)

if __name__ == '__main__':
    serv = UDPServer(('',20000) , TimeHandler)
    serv.serve_forever()