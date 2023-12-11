# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 06:54:33 2023

@author: antoi
"""

import pandas as pd
import numpy as np
import time
from scipy.linalg import pascal


#Read File
tperf=[time.time()]
file='input.txt'
dtype=np.str_
df = pd.read_csv(file,header=None) #Read ans interpreted blank line as NAN
df=df[0].apply(lambda x: pd.Series(list(x)))
M= df.to_numpy(dtype=dtype,copy=True)
Mask=(M=="#")

axis0_mask=Mask.any(axis=1)
axis1_mask=Mask.any(axis=0)

axis0=np.squeeze(np.where(np.logical_not(axis0_mask)))
axis1=np.squeeze(np.where(np.logical_not(axis1_mask)))

axis_sharp=np.squeeze(np.where(Mask)).T

k=0
for i in range(axis_sharp.shape[0]):
    temp=axis_sharp[i,0]
    k=np.searchsorted(axis0, temp)
    axis_sharp[i,0]+=k*(10**6-1)

    
k=0
for i in range(axis_sharp.shape[0]):
    temp=axis_sharp[i,1]
    k=np.searchsorted(axis1, temp)
    axis_sharp[i,1]+=k*(10**6-1)


n=axis_sharp.shape[0]
res_tab=np.zeros((n,n),dtype=np.uint64)

for i in range(n):
    for j in range(i):
        res_tab[i,j]=abs(axis_sharp[i][0]-axis_sharp[j][0])+abs(axis_sharp[i][1]-axis_sharp[j][1])
        
        
print(res_tab.sum())
#4215697168 #too low


