#!/usr/local/bin/python3

import ftplib

conn = ftplib.FTP("localhost")
conn.login("username","password") #enter appropriate username and password
data = []
conn.dir(data.append)
conn.quit()
for line in data:
  print(line)
