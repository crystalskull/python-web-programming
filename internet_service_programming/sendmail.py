#!/usr/local/bin/python3

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from_addr = '<from_address>@yahoo.com'
to_addr = '<to_address>@gmail.com'
msg = 'email sent from python3'
uname = '<user_name>'
pwd = '<password>'
mail = MIMEMultipart()
mail['From'] = from_addr
mail['To'] = to_addr
mail['Subject'] = 'Test email'
mail.attach(MIMEText(msg))
server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(uname, pwd)
server.sendmail(from_addr, to_addr, mail.as_string())
server.quit()
