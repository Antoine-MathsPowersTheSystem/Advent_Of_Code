# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 06:54:33 2023

@author: antoi
"""

import pandas as pd
import numpy as np
#Read File
names=("0","A","B","C","D","E","F","G")
df = pd.read_csv('inputb.txt',header=None,sep=":|;",engine='python',names=names) #Read ans interpreted blank line as NAN
df=df.fillna("?")
for l in names[1:]:
    df[l] = df[l].str.split(",")
   
    
nb_game=len(df["0"])
nb_set=len(names)-1



for i in range(nb_game):
    j=0
    while j<nb_set and df[names[j+1]][i]!=["?"]:
        k=0
        set_g=df[names[j+1]][i]
        l=len(set_g)
        while k<l:
            set_g[k]=set_g[k].split(" ")
            del set_g[k][0]
            set_g[k][0]=int(set_g[k][0])
            k+=1
        df[names[j+1]][i]=set_g
        j+=1


data=np.squeeze(df.to_numpy(copy=True))[:,1:]


colors=["red","green","blue"]
ok_score=np.array([12,13,14])

score=np.zeros([len(df["0"]),3],dtype=np.int32)


for i in range(nb_game):
    for j in range(nb_set):
        if data[i,j]!=["?"]:
            set_g=data[i,j]
            k=0
            while k < len(set_g):
                for l in range(3):
                    if colors[l]==set_g[k][1]: score[i,l]=np.max([set_g[k][0],score[i,l]])
                k+=1
      


mask=np.ones(nb_game,dtype=np.bool_)
for i in range(3):
    mask*=(ok_score[i]>=score[:,i])
    
sol1=np.sum(np.arange(1,nb_game+1)[mask])
#254 NO


score_prod=np.prod(score,axis=1)

sol2=np.sum(score_prod)