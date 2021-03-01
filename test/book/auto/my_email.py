#!python3
# -*- coding:utf-8 -*-


from email.mime.text import MIMEText
from email.mime.multipart import  MIMEMultipart
from smtplib import SMTP_SSL
from email.mime.base import MIMEBase
from email import encoders
from os.path import basename

SMTP_SERVER = 'smtp.naver.com'
SMTP_PORT = 465
SMTP_USER = 'xferlog'
SMTP_PASSWORD = "wpswkd1gkf"

CONTENT = '''
안녕하세요~
{} 님께서는 회비를 남부하지 않으셨습니다.
조속한 시일내에 납부부탁드립니다.
'''


def send_mail(name , addr , cc , hcc , contents , attachment = False):
    msg = MIMEMultipart('alternative')

    if attachment:
        msg = MIMEMultipart('mixed')

        text = MIMEText(contents)
        print(f'text : {text}')

        msg['From'] = SMTP_USER
        msg['To'] = addr
        msg['CC'] = cc
        msg['Subject'] = name+'님 , 메일이 도착했습니다.'
        msg.attach(text)

        file_data = MIMEBase('application' , 'octet-stream')
        with open(attachment , 'rb') as r:
            file_contents = r.read()
            file_data.set_payload(file_contents)
            encoders.encode_base64(file_data)

            filename = basename(attachment)
            file_data.add_header('Content-Disposition' , 'attachment' , filename = filename)
            msg.attach(file_data)

        taddr = ','.join((addr , cc,hcc))
        smtp = SMTP_SSL(SMTP_SERVER , SMTP_PORT)
        smtp.login(SMTP_USER , SMTP_PASSWORD)
        smtp.sendmail('xferlog@naver.com' , taddr.split(',') , msg.as_string())
        smtp.close()





if __name__ == '__main__':
    pass
    # send_mail('김철우','cwkim@zinnaworks.com',CONTENT.format('xferlog') , '테스트입니다')