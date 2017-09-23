#!/usr/local/bin/python3

import ftplib
import sys

filename = sys.argv[1]
conn = ftplib.FTP("localhost")
conn.login("username", "password") #enter appropriate username and password
with open(filename,'rb') as file:
  conn.storbinary("STOR {}".format(filename), file)
conn.quit()
