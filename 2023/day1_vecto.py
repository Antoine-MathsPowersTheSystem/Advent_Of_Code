# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 06:03:10 2023

@author: antoi
"""

import pandas as pd
import numpy as np
#Read File
df = pd.read_table('input.txt',header=None) #Read ans interpreted blank line as NAN
data=np.squeeze(df.to_numpy(copy=True)) #Transform to numpy object + delete usless dimension (squeez)

# data=np.array(["two1nine",
#     "eightwothree",
#     "abcone2threexyz",
#     "xtwone3four",
#     "4nineeightseven2",
#     "zoneight234",
#     "7pqrstsixteen"])


data=np.char.array(data,unicode=True)
data_origin=data.copy()

norm=np.array(["zero","one","two","three","four","five","six","seven","eight","nine"])

#%%


for j in range(data.size):
    chain=data[j]
    len_chain=len(chain)
    k=0
    not_found=True
    while k+3<len_chain and not_found:
        #print(chain,chain[k],type(chain[k]),chr(chain[k]))
        if "1"<=chain[k]<="9":
            not_found=False
        else:
            i=1
            while not_found and i<10:
                len_norm=len(norm[i])
                if (k+len_norm<len_chain+1) and (chain[k:k+len_norm]==norm[i]):
                    data[j]=chain[:k]+str(i)+chain[k+len_norm:]
                    not_found=False
                i+=1
        k+=1



for j in range(data.size):
    chain=data[j]
    len_chain=len(chain)
    k=len_chain-1
    not_found=True
    while k+3>0 and not_found:
        if "1"<=chain[k]<="9":
            not_found=False
        else:
            i=1
            while not_found and i<10:
                len_norm=len(norm[i])
                if (k-len_norm+2>0) and (norm[i]==chain[k-len_norm+1:k+1]):
                    data[j]=chain[:k-len_norm+1]+str(i)+chain[k+1:]
                    not_found=False
                i+=1        
        k-=1
        


#%%%
S=0
SS=np.zeros(data.size,dtype=np.uint16)
SSS=np.zeros((2,data.size),dtype=np.uint16)
i=0

    
j=np.zeros(data.size)
not_found=np.ones(data.size,dtype=np.bool_)
len_chain=np.char.str_len(data)
mask=(j< len_chain) * not_found
data=data.T
while np.any(mask):
    mask2=np.char.startswith(data,"j",0,1)
    if "1"<=chain[j]<="9":
        SSS[0,i]=ord(chain[j])-48
        not_found=False
    j+=1
        
j=len(chain)-1
not_found=True      
while -1<j and not_found:
    if "1"<=chain[j]<="9":
        SSS[1,i]=ord(chain[j])-48
        not_found=False    
    j-=1
        

    SS[i]=10*SSS[0,i]+SSS[1,i]
    S+=SS[i]
    print(i,data_origin[i],chain,SSS[:,i],SS[i],S,"\n")

    
    
print(SS.sum())



#54845 GOOD