# -*- coding: utf-8 -*-

import pandas as pd
from math import comb
import time

file = 'input.txt'

df = pd.read_csv(file, header=None, sep=" ")
df = df.T
data = [df[col].tolist() for col in df]
tperf0=time.time()
#####################################################################################################
####### Algo de personne normal avec stockage sur place (les resultats sont ecrient sur les données)
####################################################################################################
res = []
for i in range(len(data)):
    line = data[i]
    j = len(line)
    while line[:j] != [0]*j:
        for k in range(0, j-1):
            line[k] = line[k+1]-line[k]
        j-=1
    res.append(sum(line[j:]))

sol=sum(res)
tperf1=time.time()
print("Resultat:",sol)   
print("Part 1, algo naif:",round(tperf1-tperf0,6),"secondes")


##Read file 
df = pd.read_csv(file, header=None, sep=" ")
##Create list of data
data = [df[col].tolist() for col in df]
tperf2=time.time()
#########################################################################
#####      Algo math combinatoire, basé sur la transformation binomial
########################################################################

##                   (-1)^(i+j)                        sum column
solbis=sum([ pow(-1,k+len(data)+1)*comb(len(data), k)*sum(data[k]) for k in range(len(data)) ])
##                                binomial coefficient
tperf3=time.time()
print("Resultat:",solbis)   
print("Part 1, algo math:",round(tperf3-tperf2,6),"secondes")


