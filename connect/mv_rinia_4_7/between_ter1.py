import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

import os
if os.path.exists("between_ter") == False:
	os.mkdir("between_ter")

#試行回数を入力させる
print('start seed no>')
a = int(input())

print('end seed no>')
b = int(input())

#実行したsimの最大node数入力
print("max node num>")
n = int(input())


#name=['no','time','c','d','src','dst','size','h','i','j','k','l','m','n','o','p']
name=['time','size']
i=1
s=a-1

while s<b:
	s+=1
	while i<n:
	    #csvの読み込み
		node_sen=pd.read_csv("analysis_sen/Seed{0}-Node{1}group.csv" .format(s, i) ,header=0, names=name)
		node_rec=pd.read_csv("analysis_rec/Seed{0}-Node{1}group.csv" .format(s, i+1) ,header=0, names=name)
	    #node_col=受信量/送信量
		node_cal = node_rec['size'] / node_sen['size'] * 100
		node_merged = pd.concat([node_sen['time'],node_cal.fillna(0)],axis=1)
	    #csvに書き出し
		print(node_merged)
		node_merged.to_csv("between_ter/Seed{0}-Node{1}.csv" .format(s, i), header=0,index=None)
	    #グラフをプロットして保存
		node_cal.fillna(0).plot(legend=False, color='black')
		plt.xlabel("Time(Second)", fontsize=15)
		plt.ylabel("ratio(%)", fontsize=15)
		plt.xlim([0,180])
		plt.ylim([0,180])
		plt.xticks(fontsize=13)
		plt.yticks(fontsize=15)
		plt.savefig("between_ter/Seed{0}-Node{1}graph.png" .format(s, i))
	    #これやらないとメモリがやばい
		plt.close('all')
		i+=1
	i=1

