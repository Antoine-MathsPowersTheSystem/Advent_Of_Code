# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 06:54:33 2023

@author: antoi
"""

import pandas as pd
import numpy as np
import time
from scipy.linalg import pascal
dtype=np.int32

#Read File
tperf=[time.time()]
file='inputb.txt'

df = pd.read_csv(file,header=None,sep=" ") #Read ans interpreted blank line as NAN
M=df.to_numpy(dtype=dtype,copy=True)

# for i in range(M.shape[0]):
#     j=M.shape[1]
#     while np.any(M[i,:j]!=0):
#         M[i,:j-1]=M[i,1:j]-M[i,:j-1]
#         j=j-1

mask=np.any(M!=0,axis=1)
j=M.shape[1]
while np.any(mask):
    M[mask,:j-1]=M[mask,1:j]-M[mask,:j-1]
    mask=np.any(M[:,:j-1]!=0,axis=1)
    j=j-1

S=np.sum(M)   
print(M)
M=df.to_numpy(dtype=dtype,copy=True)
A=np.ones(M.shape,dtype=dtype)
A[:,0]=M[:,-1]
A2=A.copy()
for j in range(1,M.shape[1]):
    coeff=(pascal(j+1,kind='lower')[-1,:]).astype(dtype)
    coeff[(j+1)%2::2]=-coeff[(j+1)%2::2]
    for i in range(M.shape[0]):
        A[i,j]=np.dot(coeff,M[i,M.shape[1]-j-1:])
one=np.ones(M.shape[1],dtype=dtype)

Mpascal=pascal(M.shape[1],kind='lower').astype(dtype)
T=np.array([[pow(-1,j)*Mpascal[i,j] for j in range(Mpascal.shape[0])] for i in range(Mpascal.shape[1])])


for i in range(M.shape[0]):
    A2[i,:]=np.dot(T,M[i,::-1])

one=np.ones(T.shape[0])
print(np.dot(T.T,one))
T1=(pascal(7,kind='lower')[-1,:-1]).astype(dtype)
T1[::2]=-T1[::2]

for i in range(A2.shape[0]):
    print(np.dot(T1,M[i,:]))
    
sum_line=M.sum(axis=0)
print("RES",np.dot(sum_line,T1))   

#%%

M=df.to_numpy(dtype=dtype,copy=True)

mask=np.any(M!=0,axis=1)
j=0
S2=np.zeros(M.shape[0],dtype=dtype)
while np.any(mask):
    M[mask,j+1:]=M[mask,j+1:]-M[mask,j:-1]
    mask=np.any(M[:,j+1:]!=0,axis=1)
    S2[mask]=j+1
    j=j+1



M[:,::2]=-M[:,::2]
res2=M.sum()
if M.shape[1]%2==1:
    res2=-res2
print(res2)
       
        


