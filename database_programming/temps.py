#!/usr/local/bin/python3

import sqlite3 as db

conn = db.connect('test.db')
cursor = conn.cursor()
cursor.execute('drop table if exists temps')
cursor.execute('create table temps(date text, temp int)')

cursor.execute('insert into temps values("22/09/2017", 25)')
cursor.execute('insert into temps values("23/09/2017", 22)')
cursor.execute('insert into temps values("24/09/2017", 21)')
cursor.execute('insert into temps values("25/09/2017", 30)')
cursor.execute('insert into temps values("26/09/2017", 32)')
cursor.execute('insert into temps values("27/09/2017", 23)')
cursor.execute('insert into temps values("28/09/2017", 24)')

conn.row_factory = db.Row
cursor.execute('select * from temps')
rows = cursor.fetchall()
for row in rows:
  print("{:10s} {:2d}".format(row[0], row[1]))

cursor.execute('select avg(temp) from temps')
row = cursor.fetchone()
print("Average temp:{}".format(row[0]))

cursor.execute('delete from temps where temp >= 30')
cursor.execute('select * from temps')
rows = cursor.fetchall()
for row in rows:
  print("{:10s} {:2d}".format(row[0], row[1]))

cursor.execute('select avg(temp) from temps')
row = cursor.fetchone()
print("Average temp:{}".format(row[0]))

conn.close()
