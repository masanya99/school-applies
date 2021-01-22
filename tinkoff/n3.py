#!/usr/bin/env python
# coding: utf-8


n,t = map(int,input().strip().split())
floors = list(map(int,input().strip().split()))
pers = int(input())

def time_floor(n,t,floors, pers):
    if t>floors[pers-1]:
        return max(floors)-1
    else: 
        return max(floors[:pers-1]+floors[pers:])+floors[pers-1]-2
   
print(time_floor(n,t,floors, pers))


