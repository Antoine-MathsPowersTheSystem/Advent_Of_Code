# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 10:46:15 2023

@author: lucie
"""

import pandas as pd
import time
import numpy as np

df = pd.read_csv('inputb.txt',header=None,engine='python')
start = time.time()

l=df[0][0].split(':')
tcourse = [x for x in l[1].split('  ') if x != '']
temps=[]
for i in range (len(tcourse)):
    temps.append(int(tcourse[i]))
    
l1=df[0][1].split(':')
dist = [x for x in l1[1].split('  ') if x != '']
dst_rec=[]
for i in range (len(tcourse)):
    dst_rec.append(int(dist[i]))

dst_tt_course=[]
for t in temps :
    dst_course=[]
    for i in range(t):
        dst_course.append(i*(t-i))
    dst_tt_course.append(dst_course)

win=[]
for i in range(len(dst_rec)) :
    nb_win=[]
    for j in range(len(dst_tt_course[i])):
        if dst_tt_course[i][j] > dst_rec[i] :
            nb_win.append(1)
    win.append(nb_win)

wint=[]
for i in range (len(win)):
    wint.append(sum(win[i]))
    
    
d_max=np.array(dst_rec)
t_run=np.array(temps)
delta=np.sqrt(t_run**2-4*(d_max+1))
x1=(t_run-delta)/2
x2=(t_run+delta)/2
nb_push=np.around(delta,0)

np_push2=np.floor(x2)-np.ceil(x1)+1
print('solution :',np.prod(wint))

end=time.time()
print('temps',end-start)
