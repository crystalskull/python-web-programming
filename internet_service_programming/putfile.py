#!/usr/local/bin/python3

import ftplib
import sys

filename = sys.argv[1]
conn = ftplib.FTP("<FTP server url>") #use appropriate FTP server rul
conn.login("<username>", "<password>") #use appropriate username and password
with open(filename,'rb') as file:
  conn.storbinary("STOR {}".format(filename), file)
conn.quit()
