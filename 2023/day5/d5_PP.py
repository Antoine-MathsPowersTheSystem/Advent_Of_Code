# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 06:54:33 2023

@author: antoi
"""

import pandas as pd
import time

#Read File
t0=time.time()


df = pd.read_csv('inputb.txt',header=None,skip_blank_lines=True) #Read ans interpreted blank line as NAN


temp=df[0][0].split(": ")
seeds=[int(i) for i in temp[1].split()]
dic={}
key=""
names=[] 

for i in range(1 ,len(df[0])):
    line=df[0][i]
    if ":" in line:
        key=line[:-5]
        dic[key]=[]
        names.append(key)
    else:
        dic[key].append([int(j) for j in line.split()])



res=seeds.copy()

for k,x_to_y in enumerate(names):
    M=dic[x_to_y]
    for j in range(len(res)):
        for i in range(len(M)):
            dest,start,size=M[i]
            if 0<=res[j]-start<size:
                res[j]=res[j]-start+dest    
                break

print(res)     
print(min(res))

factor=100/(len(names)*len(seeds)//2)
count=0
t0=time.time()
sol=[seeds[2*i] for i in range(len(seeds)//2)]


for k,x_to_y in enumerate(names):
    M=dic[x_to_y]
    for j in range(len(seeds)//2):
        print(k,j,sol)
        start0,size0=seeds[2*j:2*j+2]
        for i in range(len(M)):
            dest,start,size=M[i]
            if start<start0<start+size:
                print(k,j,i,"case2  [",start0,",",size0+start0-1,"]","[",start,",",size+start-1,"]",)
    
                sol[j]=sol[j]-start+dest    
                break
            elif start0<=start<start0+size0:
                print(k,j,i," case1",start0,size0,dest,start,size,-start+dest)
                sol[j]=sol[j]-start+dest
                break
            elif False:
                pass

print(sol)




