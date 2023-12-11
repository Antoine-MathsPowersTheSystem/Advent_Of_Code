# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 06:54:33 2023

@author: antoi
"""

import pandas as pd
import numpy as np
import time

t0,t0_r=time.time(),time.process_time()

#Read File
names=("0","A","B","C","D","E","F")
df = pd.read_csv('input.txt',header=None,sep=":|;",engine='python',names=names) #Read ans interpreted blank line as NAN

for l in names[1:]:
    df[l] = df[l].str.split(",")
df=df.fillna("?")
   
t1,t1_r=time.time(),time.process_time()   
 
nb_game=len(df["0"])
nb_set=len(names)-1

colors=["red","green","blue"]
colors_dic={"red":0,"green":1,"blue":2}
ok_score=np.array([12,13,14])

data=np.squeeze(df.to_numpy(copy=True))[:,1:]
score=np.zeros([len(df["0"]),3],dtype=np.int32)

t2,t2_r=time.time(),time.process_time()  

for i in range(nb_game):
    j=0
    while j<nb_set and data[i,j]!="?":
        k=0
        set_g=data[i,j]
        l=len(set_g)
        while k<l:
            set_g[k]=set_g[k].split(" ")
            del set_g[k][0]
            set_g[k][0]=int(set_g[k][0])
            
            num_color=colors_dic[set_g[k][1]]

            if score[i,num_color]<set_g[k][0]: score[i,num_color]=set_g[k][0]

            k+=1
        data[i,j]=set_g
        j+=1

t3,t3_r=time.time(),time.process_time()  

mask=np.all(ok_score>=score,axis=1)
sol1=np.sum(np.arange(1,nb_game+1)[mask])



score_prod=np.prod(score,axis=1)
sol2=np.sum(score_prod)

t4,t4_r=time.time(),time.process_time()  




print(" Read time:",t1-t0,"Machin time",t1_r-t0_r)
print(" Prep data:",t2-t1,"Machin time",t2_r-t1_r)
print(" Loop time:",t3-t2,"Machin time",t3_r-t2_r)
print("Comp solut:",t4-t3,"Machin time",t4_r-t3_r)
print("Total time:",t4-t0,"Machin time",t4_r-t0_r)
print("Total time:",t4-t1,"Machin time",t4_r-t1_r,"(without read file)\n")

# print("Total time:",(t4-t0)/10**9,"Machin time",(t4_r-t0_r)/10**9,"SECONDS")
# print("Total time:",(t4-t1)/10**9,"Machin time",(t4_r-t1_r)/10**9,"SECONDS (without read file)")
# print(" Read time:",(t1-t0)/10**9,"Machin time",(t1_r-t0_r)/10**9)