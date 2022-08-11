#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 16:59:21 2022

@author: Feng
"""
'''
write the function
'''

def hello(name):
    print(name+',hello!')
    
    
def fibs(num):
    result=[0,1]
    for i in range(num-2):
        result.append(result[-2]+result[-1])
    return result

'''
recursive function
my understanding is the self-similiarity
'''
def power(x,n):
    if n==1:
        x=x
    else:
        x*=power(x,n-1)
    return x

num=10 
hello('Feng')
print('The former %s Fibb numbers are:'%num)
print(fibs(num))
print(power(2,4)