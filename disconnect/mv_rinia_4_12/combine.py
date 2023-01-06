# -*- coding: utf-8 -*
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2

from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

import os
if os.path.exists("combinegraph") == False:
	os.mkdir("combinegraph")

#試行回数を入力させる
print('seed no>')
a = int(input())

#実行したsimの最大node数入力
print("max node num>")
n = int(input())

s=0
im=[]
i=0

while s<a:
	s+=1
	while i<n:
		i+=1
		im.append(cv2.imread("analysis/Seed{0}-Node{1}graph.png" .format(s, i)))
	
	i=0
	im.append(cv2.imread("white.png"))
	im1 = cv2.vconcat([im[0]])
	im2 = cv2.vconcat([im[1]])
	im3 = cv2.vconcat([im[2]])
	im4 = cv2.vconcat([im[3]])
	im5 = cv2.hconcat([im1,im2,im3,im4])

	cv2.imwrite("combinegraph/Seed{0}CombineGraph.jpg" .format(s), im5)
	im.clear()
