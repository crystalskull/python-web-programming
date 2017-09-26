#!/usr/local/bin/python3

import imaplib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass
uname=''
pwd=''

def read():
  mail_server = imaplib.IMAP4_SSL('imap.mail.yahoo.com', 993)
  mail_server.login(uname, pwd)
  status, count = mail_server.select('Inbox')
  status, data = mail_server.fetch(count[0], '(UID BODY[TEXT])')
  print(data[0][1])
  mail_server.close()
  mail_server.logout()

def send():
  from_addr = input('From: ')
  to_addr = input('To: ')
  subject = input('Subject: ')
  msg = input('Text: ')
  mail = MIMEMultipart()
  mail['From'] = from_addr
  mail['To'] = to_addr
  mail['Subject'] = subject
  mail.attach(MIMEText(msg))
  server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
  server.ehlo()
  server.starttls()
  server.ehlo()
  server.login(uname, pwd)
  server.sendmail(from_addr, to_addr, mail.as_string())
  print('Email sent.')
  server.quit()

if __name__ == '__main__':
  print('************************')
  print('Welcome to email program')
  print('************************')
  print('Login Yahoo!:')
  uname = str(input('Username: '))
  pwd = getpass.getpass('Password:')
  while(1):
    print('===================')
    print('Enter your choice:')
    print('1. Send E-mail')
    print('2. Read E-mail')
    print('3. Exit')
    print('===================')
    opt = int(input())
    if opt == 1:
        send()
    elif opt == 2:
        read()
    elif opt == 3:
        break
