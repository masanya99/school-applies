#!/usr/bin/env python
# coding: utf-8


# 6 -3
# 5 - 3

in_data = int(input())

def cutting(n):
#     even
    if n%2==0:
        return n//2
    else:
        return n//2+1
    
print(cutting(in_data))



