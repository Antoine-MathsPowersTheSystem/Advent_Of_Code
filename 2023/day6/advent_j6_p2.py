# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 11:56:58 2023

@author: lucie
"""

import pandas as pd
import time
import numpy as np

df = pd.read_csv('input.txt',header=None,engine='python')

l=df[0][0].split(':')
tcourse =''.join([x for x in l[1].split('  ') if x != ''])
temps=''.join(tcourse.split(' '))
    
l1=df[0][1].split(':')
dist = ''.join([x for x in l1[1].split('  ') if x != ''])
dst_rec=''.join(dist.split(' '))

dst_course=[]
for t in range(int(temps)) :
        dst_course.append(t*(int(temps)-t))
        
l=0  
for d in dst_course : 
    if d > int(dst_rec):
        l+=1


print('solution :', l)
    
