#!/usr/bin/env python
# coding: utf-8
# библиотеки
import numpy as np
# входные данные
x = int(input()) #количество наборов входных данных
for i in range(x):
    N,K = map(int, input().split())
    sectors = np.array(list(map(int, input().split())))
    sums = []
    sectors= np.concatenate((sectors[K+1:],sectors[0:K]))
    length=len(sectors)
    for i in range(length):
        for j in range(length):
            if i==j:
                sums.append(sectors[i])
            else:
                sums.append(sectors[i:j+1].sum())
    print(max(sums))
    
#8 2
#2 3 4 5 -30 6 -1 2
    
#6 -1
#1 -3 2 -2 3 4