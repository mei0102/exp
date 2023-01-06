# -*- coding: utf-8 -*
#.dbcsv変換用
import sqlite3
import csv
import os

import os
if os.path.exists("csv_rec") == False:
	os.mkdir("csv_rec")
if os.path.exists("csv_sen") == False:
	os.mkdir("csv_sen")


#実行で使用したseed数入力
print("start seed num>")
s = int(input())

print("end seed num>")
b = int(input())

#実行したsimの最大seed数入力
print("max node num>")
n = int(input())

i=s-1

#seed毎に各nodeの送信パケットを抽出
#sent
while i<b:
	i+=1
	con = sqlite3.connect("seed{0}.sqlite" .format(i))
	c=con.cursor()
	j=0
	while j<n:
		j+=1
		c.execute('select * from NETWORK_Events where (NodeID is {0}) and (EventType is "NetworkSendToLower")' .format(j))
		list = c.fetchall()
		with open('csv_sen/Seed{0}-Node{1}.csv' .format(i, j),'w', newline='') as f:
			writer = csv.writer(f)
			writer.writerows(list)
	con.close()
#seed毎に各nodeの送信パケットを抽出

i=s-1
#recieve
while i<b:
	i+=1
	con = sqlite3.connect("seed{0}.sqlite" .format(i))
	c=con.cursor()
	j=0
	while j<n:
		j+=1
		c.execute('select * from NETWORK_Events where (NodeID is {0}) and (EventType is "NetworkReceiveFromLower")' .format(j))
		list = c.fetchall()
		with open('csv_rec/Seed{0}-Node{1}.csv' .format(i, j),'w', newline='') as f:
			writer = csv.writer(f)
			writer.writerows(list)
	con.close()