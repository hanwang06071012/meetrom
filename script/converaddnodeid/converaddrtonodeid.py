#!/usr/bin env python
# -*- coding: UTF-8 -*-
import re,MySQLdb

db = MySQLdb.connect("127.0.0.1","root","root","bounty",charset="utf8")
cursor = db.cursor()

source_file="selectaddr.html"
dec_file="convaddr.txt"
f_source = open(source_file,'rb')
f_dec = open(dec_file,'wb')
for sig_line in f_source.readlines():
	str_line = sig_line.strip()
	#print str_line
	matchObj = re.match(r'<li><a style="text-decoration:none;" href="/\?current_id=1">.*</a></li>',str_line,re.M | re.I)
	#matchObj = re.search(r'" href="/\?current_id=1">.*</a></li>',str_line,re.M | re.I)
	if matchObj:
		str_match = matchObj.group()
		#print str_match
		str_line1=re.sub(r'<li><a style="text-decoration:none;" href="/\?current_id=1">',"",str_match)
		str_line2 = re.sub(r'</a></li>',"",str_line1)
		#print str_line2
		str_sql = ("select node_id from node_info where name like '%%%s%%'" % str(str_line2))
		#print str_sql
		cursor.execute(str_sql)
		result = cursor.fetchall()
		for sig_node_id in result:
			node_id = sig_node_id[0]
			str_node = ("current_id=%s" % node_id)
			str_line3=re.sub(r'current_id=1',str_node,str_match)
			print str_line3
			f_dec.write(str_line3+"\n")

	else:
		print "no match!"
