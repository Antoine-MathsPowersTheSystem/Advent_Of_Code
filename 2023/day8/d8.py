# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 06:54:33 2023

@author: antoi
"""

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from math import lcm
import time

#Read File
tperf=[time.time()]
file='input.txt'
df0 = pd.read_csv(file,header=None,nrows=1)
df = pd.read_csv(file,header=None,skiprows=2,engine="python",sep=" = ") #Read ans interpreted blank line as NAN
direction={"L":0,"R":1}

nodes=df[0].to_list()
adjencies=[twoedge[1:-1].split(", ") for twoedge in df[1]]
path=[direction[direc] for direc in df0[0][0]]
dic_G={node:adjency for node,adjency in zip(nodes,adjencies)}
#%%%

# print("ok")
# node="AAA"
# i=0
# while node!="ZZZ":
#     node=dic_G[node][path[i%len(path)]]
#     i+=1
# print(i) 
#%%


l=[[nodes.index(node[0]),nodes.index(node[1])] for node in adjencies]
AStart=set(i for i,node in enumerate(nodes) if node[-1]=="A")
ZEnd=set(i for i,node in enumerate(nodes) if node[-1]=="Z")
#%%
cond=True
i=0
len_walk=[]
for node in AStart:
    i=0
    while not(node in ZEnd):
        k=path[i%len(path)]
        node=l[node][k]
        i=i+1
    print(nodes[node],i)

    len_walk.append(i)

S=len_walk[0]
S2=len_walk[0]
for i in len_walk[1:]:
    S=lcm(S,i)
    S2*=i
print(S,S2,S2//S)
# while cond and i<10**7:
#     k=path[i%len(path)]
#     AStart=set(l[j][k] for j in AStart)
#     if AStart == ZEnd: cond=False
#     I=ZEnd.intersection(AStart)
#     if len(I)>1:
#         print([nodes[i] for i in AStart],len(I))
#     i+=1


# print(i)


#%%%



G = nx.DiGraph(dic_G)
#%%%

pos = nx.spring_layout(G)
print("ok",nx.is_bipartite(G))
options = {"pos":pos,"node_color": "black", "node_size": 10,"linewidths": 0.01, "width": 0.1}


nx.draw(G, **options)

plt.savefig("graph.png",dpi=300)

#%%


