#!/usr/local/bin/python3

import ftplib

conn = ftplib.FTP("<ftp server url>") # use appropriate ftp server url
conn.login("<username>","<password>") #use appropriate username and password
data = []
conn.dir(data.append)
conn.quit()
for line in data:
  print(line)
