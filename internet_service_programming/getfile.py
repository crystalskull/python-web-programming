#!/usr/local/bin/python3

import ftplib
import sys

filename = sys.argv[1]
conn = ftplib.FTP("<FTP server url>") #use appropriate FTP server url
conn.login("<username>","<password>") #use appropriate username and password
conn.retrlines("RETR {}".format(filename))
conn.quit()
