import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

import os
if os.path.exists("jage") == False:
	os.mkdir("jage")

if os.path.exists("disconnect_time") == False:
	os.mkdir("disconnect_time")



#試行回数を入力させる
a = 1 #start
b = 10 #end
#実行したsimの最大node数入力
n = 4


#name=['no','time','c','d','src','dst','size','h','i','j','k','l','m','n','o','p']
name=['time','size']
i=1
s=a-1

while s<b:
    s+=1    
    while i<n:
        #csvの読み込み
        
        node_sen=pd.read_csv("between_ter/Seed{0}-Node{1}.csv" .format(s, i) ,header=0, names=name)
        node_ratio = node_sen[(node_sen['time'] < 181)]#180秒までの比率を抽出

        connect = node_ratio[(80 < node_ratio['size']) & (node_ratio['size'] < 112)]
        disconnect = node_ratio[(node_ratio['size'] < 80) | (node_ratio['size'] > 112)]

	    #グラフをプロットして保存
        disconnect.plot(legend=False, color='black')
        plt.xlabel("Time(Second)", fontsize=15)
        plt.ylabel("ratio(%)", fontsize=15)
        plt.xlim([0,240])
        plt.ylim([0,240])
        plt.xticks(fontsize=13)
        plt.yticks(fontsize=15)
        plt.savefig("jage/Seed{0}-Node{1}graph.jpg" .format(s, i))
	    #これやらないとメモリがやばい
        plt.close('all')
        connect.to_csv("jage/Seed{0}-Node{1}_connect.csv" .format(s, i), header=0,index=None)
        disconnect.to_csv("jage/Seed{0}-Node{1}_disconnect.csv" .format(s, i), header=0,index=None)
        i+=1
    i=1



#試行回数を入力させる
a =  1#start
b = 10 #end
#実行したsimの最大node数入力
n = 4

#name=['no','time','c','d','src','dst','size','h','i','j','k','l','m','n','o','p']
name=['time','size']
i=1
s=a-1
time = 0
time1 = 0
time2 = 0
time3 = 0
while s<b:
    s+=1    
    while i<n:
        #csvの読み込み
        node_ratio=pd.read_csv("jage/Seed{0}-Node{1}_disconnect.csv" .format(s, i) ,header=0, names=name)
        if(i == 1): time1 = (len(node_ratio))
        elif(i == 2): time2 = (len(node_ratio))
        elif(i == 3): time3 = (len(node_ratio))
        i+=1
    time = time + (time3 - time1)
    i=1
print(time/10)

