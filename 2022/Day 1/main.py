# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 16:55:22 2023

@author: antoi
"""

import numpy as np


data2=np.genfromtxt("input.dat",invalid_raise=False,usemask=False
                   ,missing_values="",filling_values=-1,dtype=int,delimiter=" ",encoding=None)

import pandas as pd
import numpy as np
#Read File
df = pd.read_csv('input.dat',skip_blank_lines=False) #Read ans interpreted blank line as NAN
df.fillna(-1, inplace=True) #Transform NAN to -1
data=np.squeeze(df.to_numpy(dtype=np.int64)) #Transform to numpy object + delete usless dimension (squeez)


nb_elves=(data==-1).sum()+1
cal_elves=np.zeros(nb_elves,dtype=np.int64)

k=0
for i in range(nb_elves):
    while (k<data.size)and(data[k]!=-1):
        cal_elves[i]+=data[k]
        k+=1
    k+=1
    
print("1. max:",cal_elves.max())
cal_elves[...]=np.sort(cal_elves)
print("2. sum of 3 max:", cal_elves[-3:].sum())