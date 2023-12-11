# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 06:54:33 2023

@author: antoi
"""

import pandas as pd
import time
import numpy as np
dtype=np.uint64
#Read File
t0=time.time()


df = pd.read_csv('inputb.txt',header=None,skip_blank_lines=True) #Read ans interpreted blank line as NAN


temp=df[0][0].split(": ")
seeds=np.array([int(i) for i in temp[1].split()],dtype=dtype)
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

for key in dic:
    dic[key]=np.array(dic[key],dtype=dtype)
    



# for i,x_to_y in enumerate(names):
#     corres=np.zeros((sizes[i],2),dtype=dtype)

#     M=dic[x_to_y]
#     S=0
#     for i in range(M.shape[0]):
#         a,b,c=M[i,:]
#         corres[S:S+c,0]=np.arange(b,b+c)
#         corres[S:S+c,1]=np.arange(a,a+c)
#         S+=c
        

#     corresponding[x_to_y]=corres

# res=seeds.copy()
# for k,x_to_y in enumerate(names):
#     M=dic[x_to_y]
#     for i in range(M.shape[0]):
#         dest,start,size=M[i,:]
#         for j in range(res.size):
#             if start<=res[j]<=start+size+1:
#                 res[j]=res[j]-start+dest
            
res=seeds.copy()

for k,x_to_y in enumerate(names):
    M=dic[x_to_y]
    for j in range(res.size):
        for i in range(M.shape[0]):
            dest,start,size=M[i,:]
            if start<=res[j]<=start+size:
                res[j]=res[j]-start+dest    
                break

print(res)     
print(res.min())

factor=100/(len(names)*seeds.size//2)
count=0
t0=time.time()
sol=np.zeros(seeds.size//2,dtype=dtype)





for l in range(seeds.size//2):
    res= np.arange(seeds[2*l],seeds[2*l]+seeds[2*l+1],dtype=dtype)
    for k,x_to_y in enumerate(names):
        #print("key=",l,round(count*factor,1),"%",round(time.time()-t0,2),"s",x_to_y)
        print(k,l,res,res.min())
        count+=1
        M=dic[x_to_y]
        mask=np.ones(res.size,dtype=np.bool_)
        for i in range(M.shape[0]):
    
            dest,start,size=M[i,:]

            mask*=(start<=res)*(res<start+size)
            res[mask]=res[mask]-start+dest
    
            mask=np.logical_not(mask)
            #print(mask)
            if mask.sum()==0: break
    
        # dest=M[:,0:1]
        # start=M[:,1:2]
        # size=M[:,2:3]
        # mask=np.ones((res.size,M.shape[0]),dtype=np.bool_)
        # #res=res[np.newaxis]
        # mask=(start<=res)*(res<start+size)
        # print("autre mask \n:",np.logical_not(mask[::-1]))
        
      
        
            
    sol[l]=np.min(res)
    print(l,res,res.min())
    print("solution possible:",sol[l])



# np.savetxt("sol2.txt", sol,fmt="%9i")    
# np.savetxt("solUlti.txt",np.array([np.min(sol)]),fmt="%9i")        
# print(np.min(sol))
#942937748 to high



# res=np.concatenate(( np.arange(seeds[0],seeds[0]+seeds[1],dtype=dtype),np.arange(seeds[2],seeds[2]+seeds[3],dtype=dtype) ))
# for l in range(seeds.size//2):
#        res= np.arange(seeds[2*l],seeds[2*l]+seeds[2*l+1],dtype=dtype)
#        for k,x_to_y in enumerate(names):
#            print("ok")
#            M=dic[x_to_y]
#            for j in range(res.size):
#                for i in range(M.shape[0]):
#                    dest,start,size=M[i,:]
#                    if start<=res[j]<=start+size:
#                        res[j]=res[j]-start+dest    
#                        break

        
# print(res.min())



# for x_to_y in names:
#     corres=np.arange(max_size)
#     print("start M extract")
#     M=dic[x_to_y]
#     print(x_to_y)
#     for i in range(M.shape[0]):
#         a,b,c=M[i,:]
#         corres[b:b+c]=np.arange(a,a+c)

#     corresponding[x_to_y]=corres
# print("ok1")
# res=seeds    
# for x_to_y in names:
    
#     res=corresponding[x_to_y][res]
# print("ok2")
# sol=np.min(res)
# print(sol)

