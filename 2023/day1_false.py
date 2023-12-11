# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 06:03:10 2023

@author: antoi
"""

import pandas as pd
import numpy as np
#Read File
df = pd.read_table('input.txt',header=None) #Read ans interpreted blank line as NAN
#df.fillna(-1, inplace=True) #Transform NAN to -1
data_origin=np.squeeze(df.to_numpy().copy())
data_f=np.squeeze(df.to_numpy().copy()) #Transform to numpy object + delete usless dimension (squeez)

# data=np.array(["two1nine",
#     "eightwothree",
#     "abcone2threexyz",
#     "xtwone3four",
#     "4nineeightseven2",
#     "zoneight234",
#     "7pqrstsixteen","3two3eightjszbfourkxbh5twonepr"])
data_origin=data_f.copy()

norm=np.array(["zero","one","two","three","four","five","six","seven","eight","nine"])
#%%%
# for j in range(data.size):
#     for i in range(10):
#         k=0
#         chain=data[j]
#         while norm[i] in chain:
#             print(j,i)
#             while chain[k:k+len(norm[i])]!=norm[i]:
#                 k+=1
#             chain=chain[:k]+str(i)+chain[k+len(norm[i]):]
#             data[j]=chain
#             print("\n",data_origin[j],"\n",data[j])
#%%


for j in range(data_f.size):
    chain=data_f[j]
    k=0
    not_found=True
    while k+3<len(chain) and not_found:
        if "1"<=chain[k]<="9":
            not_found=True
        else:
            for i in range(1,10):
                if k+len(norm[i])<len(chain)+1:
                    if chain[k:k+len(norm[i])]==norm[i]:
                        chain=chain[:k]+str(i)+chain[k+len(norm[i]):]
                        data_f[j]=chain
                        not_found=False
                        print("\n",data_origin[j],"\n",data_f[j])
        k+=1

for j in range(data_f.size):
    chain=data_f[j]
    k=len(chain)-1
    not_found=True
    while k+3>0 and not_found:
        if "1"<=chain[k]<="9":
            not_found=True
        else:
            for i in range(1,10):
                if k-len(norm[i])+2>0:
                    if norm[i]==chain[k-len(norm[i])+1:k+1]:
                        
                        chain=chain[:k-len(norm[i])+1]+str(i)+chain[k+1:]
                        data_f[j]=chain
                        not_found=False
                        print("\n",data_origin[j],"\n",data_f[j])
        k-=1
        



      
#Read left to tright
# for j in range(data.size):
#       chain=data[j]
#       k=0
#       not_found=True
#       while k<len(chain):
#           for i in range(1,10):
#               if chain[k:k+len(norm[i])]==norm[i]:
#                   chain=chain[:k]+str(i)+chain[k+len(norm[i]):]
#                   data[j]=chain
#                   not_found=False
#                   print("\n",data_origin[j],"\n",data[j])
#           k+=1   
#%%%
#Read right to lef
# for j in range(data.size):
#     chain=data[j]
#     k=len(chain)-1
#     not_found=True
#     while k>0 :
#         for i in range(1,10):
#             if norm[i]==chain[k-len(norm[i])+1:k+1]:           
#                 chain=chain[:k-len(norm[i])+1]+str(i)+chain[k+1:]
#                 data[j]=chain
#                 not_found=False
#                 print("\n",data_origin[j],"\n",data[j])
#         k-=1
#%%%
data_origin=np.squeeze(df.to_numpy().copy())
data=np.squeeze(df.to_numpy().copy()) #Transform to numpy object + delete usless dimension (squeez)

# data=np.array(["two1nine",
#     "eightwothree",
#     "abcone2threexyz",
#     "xtwone3four",
#     "4nineeightseven2",
#     "zoneight234",
#     "7pqrstsixteen","3two3eightjszbfourkxbh5twonepr"])
data_origin=data.copy()

norm=np.array(["zero","one","two","three","four","five","six","seven","eight","nine"])

#%%


for j in range(data.size):
    chain=data[j]
    k=0
    not_found=True
    while k+3<len(chain) and not_found:
        if "1"<=chain[k]<="9":
            not_found=False
        else:
            for i in range(1,10):
                if k+len(norm[i])<len(chain)+1:
                    if chain[k:k+len(norm[i])]==norm[i]:
                        chain=chain[:k]+str(i)+chain[k+len(norm[i]):]
                        data[j]=chain
                        not_found=False
                        print("\n",data_origin[j],"\n",data[j])
        k+=1

for j in range(data.size):
    chain=data[j]
    k=len(chain)-1
    not_found=True
    while k+3>0 and not_found:
        if "1"<=chain[k]<="9":
            not_found=False
        else:
            for i in range(1,10):
                if k-len(norm[i])+2>0:
                    if norm[i]==chain[k-len(norm[i])+1:k+1]:
                        
                        chain=chain[:k-len(norm[i])+1]+str(i)+chain[k+1:]
                        data[j]=chain
                        not_found=False
                        print("\n",data_origin[j],"\n",data[j])
        k-=1


S=0
SS=np.zeros(data_f.size)
i=0
for chain in data_f:
    temp=[]
    for char in chain:
        if "1"<=char<="9":
            x=ord(char)-48
            temp.append(x)


    if len(temp)>0:
        S+=(temp[-1]+10*temp[0])
    SS[i]=temp[-1]+10*temp[0]
    
    i+=1
    print(i-1,data_origin[i-1],chain,temp,temp[-1]+10*temp[0],S,"\n")
    
 
S=0
SS0=np.zeros(data.size)
i=0
for chain in data:
    temp=[]
    for char in chain:
        if "1"<=char<="9":
            x=ord(char)-48
            temp.append(x)


    if len(temp)>0:
        S+=(temp[-1]+10*temp[0])
    SS0[i]=temp[-1]+10*temp[0]
    i+=1
    print(i-1,data_origin[i-1],chain,temp,temp[-1]+10*temp[0],S,"\n")   
 

print(SS.sum())
#54100 avec normalistation
#55079 sans

#54655
#54826
#54871 trop grand

mask=SS!=SS0
data=data[mask]
data_f=data_f[mask]
data_origin=data_origin[mask]
for i in range(mask.sum()):
    print("original\n",data_origin[i],"\nfalse\n",data_f[i],"\ntrue\n",data[i],"\n")
