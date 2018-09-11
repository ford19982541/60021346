# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 20:51:48 2018

@author: shiss
"""

data_1 = open('data_input.txt','r')
list_in = []
list_out = []
for line in data_1 :
    l = line.split()
    list_in.append(int(l[1]))
    list_out.append(l)
data_1.close()
start = 1
while start < len(list_in):
    j =start -1
    while(j>=0):
        if(list_in[j] <= list_in[j+1]):
            break
        else:
            list_in[j],list_in[j+1] =list_in[j+1],list_in[j]
            list_out[j],list_out[j+1] =list_out[j+1],list_out[j]
        j -= 1
    start += 1
    
out = open('data_output.txt','w')
out.write(str(list_out))
out.close()

