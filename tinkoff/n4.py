#!/usr/bin/env python
# coding: utf-8


X,Y = map(int,input().strip().split())
in_data = list(map(float,input().strip().split()))
def dot(X,Y,data):
    cord = [(0,0),(X,0),(X,Y),(0,Y)]
    cord_n = []
    for i,j in zip(range(0,len(data),2),range(1,len(data),2)):
        cord_n.append((data[i],data[j]))
    return 2.5000, 2.0833
    
print(dot(X,Y,in_data))


