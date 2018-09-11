# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 11:08:31 2018

@author: shiss
"""
sumscore = 0
countline = 0
with open('input.txt','r',encoding = 'utf-8') as myinput :
    for line in myinput :
        l = line.split()
        score = int(l[1])
        sumscore += score
        countline += 1
        
    if (countline != 0):
        avg = sumscore / countline
    else :
        avg = 0 
with open('ss.txt','w',encoding = 'utf-8') as file :
    file.write('ค่าเฉลี่ย = ')
    file.write(str(avg))
    print(file.read())