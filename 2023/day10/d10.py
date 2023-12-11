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
L= df.to_numpy(dtype=dtype,copy=True)
M=df.to_numpy(dtype=dtype,copy=True)
M=M[::-1,:]
pipe=np.array(list('|-'),dtype=dtype)
move=np.array(list('LJ7F'),dtype=dtype)
mask_way=np.zeros(M.shape,dtype=np.bool_)     

view=np.zeros(M.shape,dtype=np.uint16)

temp=np.array([[0,1],[0,-1],[1,0],[-1,0]],dtype=np.int32)

start=np.squeeze(np.where(M=='S'))
pos=np.zeros((4,2),dtype=np.uint32)
i=0
if M[tuple(start+temp[i])] in '-J7':
    pos[i]=start+temp[i]
i=1
if M[tuple(start+temp[i])] in '-LF':
    pos[i]=start+temp[i]
i=2
if M[tuple(start+temp[i])] in '|7F':
    pos[i]=start+temp[i]
i=3
if M[tuple(start+temp[i])] in '|LJ':
    pos[i]=start+temp[i]

pos=np.sort(np.reshape(pos[pos!=0],(2,-1)),axis=0)

print(start)
print(M[tuple(pos[0])],pos[0])
print(M[tuple(pos[1])],pos[1])
print(M[start[0]-1:start[0]+2,start[1]-1:start[1]+2][::-1])
startchar="J"



#%%

        
def dir(M,actual_dir,old_dir):
    result=actual_dir.copy()
    char=M[tuple(actual_dir)]
            
    if actual_dir[0]==old_dir[0]:
        if char in "LJ":
            result[0]+=1
            return result
        elif char in "7F":
            result[0]-=1
            return result
        
    elif actual_dir[1]==old_dir[1]:
        if char in "LF":
            result[1]+=1
            return result
        elif char in "J7":
            result[1]-=1
            return result
        
        
    if char=="|":
        if old_dir[0]>actual_dir[0]:
            result[0]-=1
            return result 
        else: 
            result[0]+=1
            return result
    elif char=="-":
        if old_dir[1]>actual_dir[1]:
            result[1]-=1
            return result
        else: 
            result[1]+=1
            return result        
    print("error")
        
old_pos=start.copy()
i=0
pos=pos[1]
mask_way[tuple(pos)]=True

while np.any(pos!=start):
    new_pos=dir(M,pos,old_pos)
    old_pos=pos.copy()
    pos=new_pos.copy()
    mask_way[tuple(pos)]=True
    i+=1
    
print(i//2+1)       
        
M[tuple(start)]=startchar
elem_line=np.zeros(M.shape[0],dtype=np.uint32)
for i in range(M.shape[0]):
    k=0
    interrior=False
    enter=''
    for j in range(M.shape[1]):
        if mask_way[i,j]:
            if M[i,j] == "|":
                interrior=not(interrior)
                view[i,j]=1
            elif M[i,j] in 'LJ7F':
                if len(enter)>0:
                    if M[i,j]=='7' and enter=='L':
                        interrior=not(interrior)
                    if M[i,j]=='J' and enter=='F':
                        interrior=not(interrior)
                    enter=''
                else:
                    enter=M[i,j]

                
        elif interrior:
            k+=1
            view[i,j]=6
    elem_line[i]=k


A1=M[::-1]
A2=view[::-1]


print(elem_line.sum())





        