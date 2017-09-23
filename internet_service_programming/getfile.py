#!/usr/local/bin/python3

import ftplib
import sys

filename = sys.argv[1]
conn = ftplib.FTP("localhost")
conn.login("username","password") #enter appropriate username and password
conn.retrlines("RETR {}".format(filename))
conn.quit()
