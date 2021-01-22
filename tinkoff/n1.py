#!/usr/bin/env python
# coding: utf-8


'''стоимость тарифа Кости, 
размер тарифа Кости, 
стоимость каждого лишнего мегабайта, 
размер интернет-трафика Кости в следующем месяце'''
# 100 10 12 15
# 100 10 12 1

in_data = list(map(int,input().strip().split()))

def tarif(data):
    overload = 0
    
    if data[3]>data[1]:
        overload = data[3] - data[1]
        
    return data[0]+data[2] *overload 

print(tarif(in_data))



