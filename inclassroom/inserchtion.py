# -*- coding: utf-8 -*-

L =[5,6,7,1,4,2,9,3,8]

start = 1
while start < len(L):
    j =start -1
    while(j>=0):
        print(j)
        if(L[j] <= L[j+1]):
            break
        else:
            L[j],L[j+1] =L[j+1],L[j]
            
        j -= 1
    start += 1