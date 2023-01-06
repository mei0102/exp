import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

import os
if os.path.exists("whole") == False:
	os.mkdir("whole")

#name=['no','time','c','d','src','dst','size','h','i','j','k','l','m','n','o','p']
name=['time','size']
sen_sum = 0
rec_sum = 0
i=1

#試行回数を入力させる
print('seed no>')
a = int(input())

#実行したsimの最大node数入力
print("max node num>")
n = int(input())

s=0

while s<a:
	s+=1
	while i<n+1:
	    #csvの読み込み
	    node_sen=pd.read_csv("analysis_sen/Seed{0}-Node{1}group.csv" .format(s, i) ,header=0, names=name)
	    node_rec=pd.read_csv("analysis_rec/Seed{0}-Node{1}group.csv" .format(s, i) ,header=0, names=name)
	    sen_sum += node_sen['size']
	    rec_sum += node_rec['size']
	    i += 1
	i=1
	#node_col=受信量/送信量
	node_cal = rec_sum / sen_sum * 100
	print(node_cal)
	#csvに書き出し
	node_cal.to_csv("whole/Seed{0}-Node{1}.csv" .format(s, i), header=0,index=None)
	#グラフをプロットして保存
	node_cal.fillna(0).plot(legend=False, color='black')
	plt.xlabel("Time(Second)", fontsize=15)
	plt.ylabel("ratio(%)", fontsize=15)
	plt.xlim([0,240])
	plt.ylim([0,240])
	plt.xticks(fontsize=13)
	plt.yticks(fontsize=15)
	plt.savefig("whole/Seed{0}-Node{1}graph.png" .format(s, i))
	#これやらないとメモリがやばい
	plt.close('all')
	
