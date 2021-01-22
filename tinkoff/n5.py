#!/usr/bin/env python
# coding: utf-8


n = int(input())
in_data = []
for i in range(n):
    in_data.append(int(input()))

def price(data):
    suma = []
    coupons_n = []
    
    for n, el in enumerate(data):
        if el > 100:
            coupons_n.append(n)
    
    if len(coupons_n)==0:
        return sum(data)
    elif (len(coupons_n)==1) or (coupons_n[1]==len(data)-1):
        return sum(data[:coupons_n[0]])+sum(data[coupons_n[0]:])-max(data[coupons_n[0]+1:])


print(price(in_data))


