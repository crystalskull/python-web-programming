#!/usr/local/bin/python3

import sqlite3 as db

conn = db.connect('test.db')
cursor = conn.cursor()
cursor.execute("create table films(name text, year text, director text)")
print('table created')
conn.close()
