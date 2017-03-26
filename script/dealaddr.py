#!/usr/bin/python
# -*- coding: UTF-8 -*-
#######################################################
#filename:test_xlutils.py
#author:defias
#date:xxxx-xx-xx
#function：向excel文件中写入数据
#######################################################
import xlrd
import xlutils.copy
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
#打开一个workbook
map_node={"58同城":{"name":"58同城","parent_id":0,"node_id":0}}
rb = xlrd.open_workbook('addrs.xls')
raddr = rb.sheet_by_name('Sheet2')
num_rows = raddr.nrows
num_cols = raddr.ncols
print ("num_rows=%d,num_cols=%d"%(num_rows,num_cols))
wb = xlutils.copy.copy(rb)
ws = wb.get_sheet(2)
str_cp =''
for i in range(num_cols):
	for j in range(num_rows):
		str_addr = raddr.cell_value(j,i).strip()
		int_map_len = len(map_node)
		if(i==0):
			if not map_node.has_key(str_addr):
				map_node[str_addr]={"name":str_addr,"parent_id":0,"node_id":int_map_len}
			else:
				pass
		elif(i==1):
			if not map_node.has_key(str_addr):
				str_addr_sheng = raddr.cell_value(j,0).strip()
				str_parent_id = map_node[str_addr_sheng]
				map_node[str_addr]={"name":str_addr,"parent_id":str_parent_id["node_id"],"node_id":int_map_len}
		else:
			if not map_node.has_key(str_addr):
				str_addr_shi = raddr.cell_value(j,1).strip()
				str_parent_id = map_node[str_addr_shi]
				map_node[str_addr]={"name":str_addr,"parent_id":str_parent_id["node_id"],"node_id":int_map_len}
print map_node
db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="bounty", charset="utf8")
# 使用cursor()方法获取操作游标 
cursor = db.cursor()
for v in map_node.values():
	str_sql = ("insert into node_info (name,node_id,parent_id,addris,timemodify) values ('%s','%d','%d','%d',now());"%(v['name'],v['node_id'],v['parent_id'],1))
	cursor.execute(str_sql)
	db.commit()
	print str_sql
cursor.close()
db.close()
wb.save('addrs.xls')
#wb = xlutils.copy.copy(rb)
#获取sheet对象，通过sheet_by_index()获取的sheet对象没有write()方法
#ws = wb.get_sheet(0)
#写入数据
#ws.write(1, 1, 'changed!')
#添加sheet页
#wb.add_sheet('sheetnnn2',cell_overwrite_ok=True)
#利用保存时同名覆盖达到修改excel文件的目的,注意未被修改的内容保持不变
#wb.save('/home/hanwang/Desktop/addrs.xls')
