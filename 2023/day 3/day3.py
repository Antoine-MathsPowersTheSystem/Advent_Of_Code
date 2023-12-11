# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 06:54:33 2023

@author: antoi
"""

import pandas as pd
import numpy as np
import time
#Read File

t0=time.time()
df = pd.read_csv('input.txt',header=None,engine='python') #Read ans interpreted blank line as NAN
for i in range(df.size):
     df[0][i]=list(df[0][i])
    
data_b=df[0].to_list()
data=np.array(data_b)

t1=time.time()

dim_data=data.shape

data_aug=np.zeros((dim_data[0]+2,dim_data[1]+2),dtype=np.str_)
data_aug[...]="."
data_aug[1:-1,1:-1]=data
score=np.zeros(dim_data[0])


for i in range(dim_data[0]):
    k=1
    for j in range(dim_data[1]):
        if k==1:
            if data[i,j].isnumeric() :
                is_valid=False
                temp=[int(data[i,j])]
                while k+j<dim_data[1] and data[i,j+k].isnumeric():
                    temp.append(int(data[i,j+k]))
                    k+=1
                    
                for l in range(1,k+1):
                    for m in range(3):
                        for n in range(3):
                            if m!=1 or n!=1:
                                regard=data_aug[i+m,j+l-1+n]
                                if not(regard.isnumeric()) and not(regard=="."):
                                    is_valid=True
                if is_valid:
                    score[i]+=np.sum(np.array(temp)[::-1]*10**np.arange(k))
        else:
            k-=1

sol=np.sum(score)
t2=time.time()

mask=(data=="*")
nb_star=mask.sum()
pos_star=np.stack(np.where(mask),axis=-1)
ratio=np.empty_like(pos_star)
ratio[...]=0

for alpha in range(nb_star):
    i,j=pos_star[alpha,:]
    for m in range(3):
        posv=i+m
        line=data_aug[posv,:]
        for n in range(3):
            if m!=1 or n!=1:
                posh=j+n
                regard=line[posh]
                if regard.isnumeric():

                    cursl=posh-1
                    cursr=posh+1
                    while line[cursr].isnumeric():
                        cursr+=1
                    while line[cursl].isnumeric():
                        cursl-=1
                    num=line[cursl+1:cursr].astype(np.int16)
                    num=np.sum(num[::-1]*10**np.arange(cursr-cursl-1))

                    if ratio[alpha,0]==0:
                        ratio[alpha,0]=num
                    else:
                        ratio[alpha,1]=num
                        
                    line[cursl+1:cursr]="."
                
mask= ratio !=0
mask=np.all(mask,axis=1)           
prod=np.prod(ratio[mask,:],axis=1)

sol2=np.sum(prod)
t3=time.time()

print("read file",t1-t0)
print("     sol1",t2-t1)
print("     sol2",t3-t2)
print("      tot",t3-t0)
