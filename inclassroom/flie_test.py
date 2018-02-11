# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 13:49:38 2018

@author: Student
"""
sumscore = 0
countline = 0
f = open('input.txt','r',encoding='utf8')
for line in f :
    l = line.split()
    score = int(l[1])
    sumscore += score
    countline += 1
f.close()

if (countline != 0):
    avg = sumscore / countline
else :
    avg = 0

out = open('output.txt','w',encoding='utf8')
out.write(u'ค่าเฉลี่ย  = ')
out.write(str(avg))
out.close()