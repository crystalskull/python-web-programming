#!/usr/local/bin/python3

import imaplib

mail_server = imaplib.IMAP4_SSL('imap.mail.yahoo.com', 993)
user_name = '<user_name>@yahoo.com'
password = '<password>'

mail_server.login(user_name, password)
status, count = mail_server.select('Inbox')
status, data = mail_server.fetch(count[0], '(UID BODY[TEXT])')
print(data[0][1])

mail_server.close()
mail_server.logout()
