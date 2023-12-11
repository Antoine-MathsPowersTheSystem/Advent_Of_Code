# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 06:54:33 2023

@author: antoi
"""

import pandas as pd
import time
import numpy as np
#Read File
t0=time.time()
df = pd.read_csv('input.txt',header=None,sep=":") #Read ans interpreted blank line as NAN

l1=[]
l2=[]
for i in range(len(df[1])):

    chain=df[1][i]
    chain=chain.split("|")

    for j in range(2):
        chain[j]=chain[j].split(' ')

        while '' in chain[j]:
            chain[j].remove('')
        for k in range(len(chain[j])):
            chain[j][k]=int(chain[j][k])
    l1.append(chain[0])
    l2.append(chain[1])

#%%Part2
t1=time.time()
data1=np.array(l1)
data2=np.array(l2)



mask=np.zeros(data1.shape,dtype=np.bool_)

for i in range(data1.shape[0]): mask[i,:]=np.isin(data1[i,:],data2[i,:])
# mask=np.isin(data1,data2,axis=0)

card_win=2**(mask.sum(axis=1))
card_win[card_win==1]=0
card_win=card_win/2

sol=np.sum(card_win)
#%%Part 2
t2=time.time()


mask1=mask.sum(axis=1)
multiplicité=np.ones(data1.shape[0],dtype=np.uint32)


for i1 in range(data1.shape[0]): multiplicité[i1+1:i1+mask1[i1]+1]+=multiplicité[i1]
  
    
sol2=multiplicité.sum()
#8549735  
t3=time.time()



print("read file",t1-t0)
print("     sol1",t2-t1)
print("     sol2",t3-t2)
print("      tot",t3-t0)

    
    
    
    
    
    