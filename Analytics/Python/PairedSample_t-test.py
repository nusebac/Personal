# -*- coding: utf-8 -*-
"""
@author: Arka
"""
from __future__ import division
import pandas as pd

data = pd.ExcelFile("C:/Users/HP/Desktop/Book1.xlsx")
newfile =data.parse('Sheet1')

sum_d=0
sum_d_square=0
N = len(newfile)
# List the raw scores by group.
# Subtract each Y score from each X score (d).
# Square each d and sum.
for i in range(len(newfile)):
    d = newfile[newfile.columns[0]][i] - newfile[newfile.columns[1]][i]
    d_square = d**2
    sum_d += d 
    sum_d_square += d_square    
# Formula to calculate the t-ratio.
t_ratio = (sum_d/N)/((sum_d_square -((sum_d**2)/N))/N*(N-1))**(1/2)
print "The value of T- Ratio is :  %s"%(str(t_ratio))
df = N-1
print "The degree of frredom is :  %s "%(str(df))
# Crtical table for T-Test
if df >= 17 and df < 18:
    if t_ratio > 2.11 and t_ratio < 2.90:
        print "Test is significant with P-vale < 0.05"
    elif t_ratio > 2.90:
        print "Test is highly significant with P-vale < 0.01"
    else:
        print "T- Test is not significanct P-vale > 0.05"
elif df >= 18 and df < 19:
    if t_ratio > 2.10 and t_ratio < 2.88:
        print "Test is significant with P-vale < 0.05"
    elif t_ratio > 2.88:
        print "Test is highly significant with P-vale < 0.01"
    else:
        print "T- Test is not significanct P-vale > 0.05"
elif df >= 19 and df < 20:
    if t_ratio > 2.09 and t_ratio < 2.86:
        print "Test is significant with P-vale < 0.05"
    elif t_ratio > 2.86:
        print "Test is highly significant with P-vale < 0.01"
    else:
        print "T- Test is not significanct P-vale > 0.05"
elif df >= 20 and df < 23:
    if t_ratio > 2.09 and t_ratio < 2.84:
        print "Test is significant with P-vale < 0.05"
    elif t_ratio > 2.84:
        print "Test is highly significant with P-vale < 0.01"
    else:
        print "T- Test is not significanct P-vale > 0.05"
elif df >= 23 and df < 30:
    if t_ratio > 2.06 and t_ratio < 2.79:
        print "Test is significant with P-vale < 0.05"
    elif t_ratio > 2.79:
        print "Test is highly significant with P-vale < 0.01"
    else:
        print "T- Test is not significanct P-vale > 0.05"
elif df >= 30 and df < 40:
    if t_ratio > 2.04 and t_ratio < 2.75:
        print "Test is significant with P-vale < 0.05"
    elif t_ratio > 2.75:
        print "Test is highly significant with P-vale < 0.01"
    else:
        print "T- Test is not significanct P-vale > 0.05"
elif df >= 40 and df < 50:
    if t_ratio > 2.02 and t_ratio < 2.7:
        print "Test is significant with P-vale < 0.05"
    elif t_ratio > 2.7:
        print "Test is highly significant with P-vale < 0.01"
    else:
        print "T- Test is not significanct P-vale > 0.05"
elif df >= 50 and df < 100:
    if t_ratio > 2.01 and t_ratio < 2.68:
        print "Test is significant with P-vale < 0.05"
    elif t_ratio > 2.68:
        print "Test is highly significant with P-vale < 0.01"
    else:
        print "T- Test is not significanct P-vale > 0.05"
elif df >= 100:
    if t_ratio > 1.98 and t_ratio < 2.63:
        print "Test is significant with P-vale < 0.05"
    elif t_ratio > 2.63:
        print "Test is highly significant with P-vale < 0.01"
    else:
        print "T- Test is not significanct P-vale > 0.05"


    




