import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

import os
if os.path.exists("analysis_sen") == False:
	os.mkdir("analysis_sen")
if os.path.exists("analysis_rec") == False:
	os.mkdir("analysis_rec")

#試行回数を入力させる
print('start seed no>')
a = int(input())

print('end seed no>')
b = int(input())

#実行したsimの最大node数入力
print("max node num>")
n = int(input())

#各種初期化
i=0
s=a-1

#name=['no','time','c','d','src','dst','size','h','i','j','k','l','m','n','o','p']
name=['time','size']

#seed回数実行
while s<b:
	s+=1
	#Node回数実行
	while i<n:
		j=0
		i+=1
		#sen
		#csvの読み込み
		node=pd.read_csv("csv_sen/Seed{0}-Node{1}.csv" .format(s, i), header=None, usecols=[1,6], names=name)
		#空行を埋めるために各秒数にsize0の行を挿入
		while j<181:
			node = node.append(pd.DataFrame({'time' :[j]}))
			j+=1
		node['time'] = np.ceil(node['time'])
		#整数値に直してる
		#グループ化してcsvに書き出し
		node=node.groupby('time')[['size']].sum()
		#合計してる
		#kbpsに直す
		node['size']*=8
		node['size']/=1000
		#グラフをプロットして保存
		node.plot(legend=False, color='black')
		plt.xlabel("Time(Second)", fontsize=15)
		plt.ylabel("Size(KBit)", fontsize=15)
		plt.xlim([0,180])
		plt.ylim([0,180])
		plt.xticks(fontsize=15)
		plt.yticks(fontsize=15)
		plt.savefig("analysis_sen/Seed{0}-Node{1}graph.png" .format(s, i))
		#これやらないとメモリがやばい
		plt.close('all')
		node.to_csv("analysis_sen/Seed{0}-Node{1}group.csv" .format(s, i))
		
	i=0

#各種初期化
i=0
s=a-1

#name=['no','time','c','d','src','dst','size','h','i','j','k','l','m','n','o','p']
name=['time','size']

#seed回数実行
while s<b:
	s+=1
	#Node回数実行
	while i<n:
		j=0
		i+=1
		#rec
		#csvの読み込み
		node=pd.read_csv("csv_rec/Seed{0}-Node{1}.csv" .format(s, i), header=None, usecols=[1,6], names=name)
		#空行を埋めるために各秒数にsize0の行を挿入
		while j<181:
			node = node.append(pd.DataFrame({'time' :[j]}))
			j+=1
		node['time'] = np.ceil(node['time'])
		#整数値に直してる
		#グループ化してcsvに書き出し
		node=node.groupby('time')[['size']].sum()
		#合計してる
		#kbpsに直す
		node['size']*=8
		node['size']/=1000
		#グラフをプロットして保存
		node.plot(legend=False, color='black')
		plt.xlabel("Time(Second)", fontsize=15)
		plt.ylabel("Size(KBit)", fontsize=15)
		plt.xlim([0,180])
		plt.ylim([0,180])
		plt.xticks(fontsize=15)
		plt.yticks(fontsize=15)
		plt.savefig("analysis_rec/Seed{0}-Node{1}graph.png" .format(s, i))
		#これやらないとメモリがやばい
		plt.close('all')
		node.to_csv("analysis_rec/Seed{0}-Node{1}group.csv" .format(s, i))
	i=0
