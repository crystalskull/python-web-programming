#!/usr/local/bin/python3

from nntplib import NNTP

server = NNTP('news.aioe.org')
resp, count, first, last, name = server.group('sci.logic')
print('Group', name, 'has', count, 'articles, range', first, 'to', last)
resp, subs = server.xhdr('subject',str(first) + '-' + str(last))
for id, text in subs[-10:]:
  print(id,text)
