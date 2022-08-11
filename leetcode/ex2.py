import numpy as np
'''
Two ways to show the control flow:
while loop
if loop
'''

str='abcxyzx'
j=0
count=0
while j<len(str):
    if str[j]=='x':
        print(str[j])
        count+=1
    j+=1
        
    
print(len(str),count) 
    
