# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 06:54:33 2023

@author: antoi
"""

import pandas as pd
import numpy as np
import time

type_u=np.uint32
#Read File

t0=time.time()
df = pd.read_csv('inputb.txt',header=None,dtype=str) #Read ans interpreted blank line as NAN
t1=time.time()
for i in range(df.size):
     df[0][i]=list(df[0][i])
    
data_b=df[0].to_list()
data=np.array(data_b).astype(np.bool_)
shape=data.shape


temp=np.sum(data,axis=0,dtype=type_u)
mask=temp>shape[0]/2
if mask.sum(dtype=type_u)>shape[1]/2:
    key1=mask
    key2=np.logical_not(mask)
else:
    key1=np.logical_not(mask)
    key2=mask

num1=np.sum(2**np.arange(key1.size-1,-1,step=-1 ,dtype=type_u)[key1],dtype=type_u)
num2=np.sum(2**np.arange(key1.size-1,-1,step=-1 ,dtype=type_u)[key2],dtype=type_u)
# dim_data=data.shape

res=num1*num2
print(res)



data_work=data.copy()
pos=np.arange(data.shape[0])
cond=True
while cond:
    mask=data_work[:,0]
    S=np.sum(mask)
    if S>=mask.size/2:
        data_work=data_work[mask,1:]
        pos=pos[mask]
    else:
        data_work=data_work[np.logical_not(mask),1:]
        pos=pos[np.logical_not(mask)]
        
    cond=pos.size>1

print(data[pos,:],S)
key1=np.squeeze(data[pos[0],:])
num1=np.sum(2**np.arange(key1.size-1,-1,step=-1 ,dtype=type_u)[key1],dtype=type_u)



data_work=data.copy()
pos=np.arange(data.shape[0])
cond=True
while cond:
    mask=data_work[:,0]
    S=np.sum(mask)
    if S<mask.size/2:
        data_work=data_work[mask,:]
        pos=pos[mask]
    else:
        data_work=data_work[np.logical_not(mask),:]
        pos=pos[np.logical_not(mask)]
        
    data_work=data_work[:,1:]
    cond=pos.size>1


print(data[pos,:])
key2=np.squeeze(data[pos[0],:])
num2=np.sum(2**np.arange(key2.size-1,-1,step=-1 ,dtype=type_u)[key2],dtype=type_u)


ratio=num1*num2
print(ratio)