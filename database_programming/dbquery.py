#!/usr/local/bin/python3

import sqlite3 as db

conn = db.connect('test.db')
conn.row_factory = db.Row
cursor = conn.cursor()

cursor.execute('select * from films')
rows = cursor.fetchall()
for row in rows:
  print("{:30s} {:4s} {:30s}".format(row['name'], row['year'], row['director']))

conn.close()
