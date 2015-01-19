# -*- coding: utf-8 -*-
"""
@author: Arka
"""
from __future__ import division
import pandas as pd


data = pd.ExcelFile("C:/Users/HP/Desktop/Book1.xlsx")
newdata=data.parse('Sheet1')

# Mean : Average = (Sum of all the values)/number of values
# Median : -->Arrange data by least to greatest -->eliminate the extreme values -->if the leftover is two values then average them 
# Mode:  The most repeated value
# Range: Largest Value - Smallest Value
# Variance: Variance = (Sum((X-MeanOfX)^2))/N-1
# Standard Deviation: SD = (Variance)^(1/2)

unorderlist=[]
suming_variance=0
for i in range(len(newdata.columns)):
    mean = sum(newdata[newdata.columns[i]])/(len(newdata[newdata.columns[i]]))
    print "----------------------------------START %s-------------------------------------------"%(str(newdata.columns[i]))
    print "The mean for %s is : %s"%(str(newdata.columns[i]),str(mean))
    for j in range(len(newdata[newdata.columns[i]])):
        unorderlist.append(newdata[newdata.columns[i]][j])
        diff_mean = (newdata[newdata.columns[i]][j] - mean)**2
        suming_variance+=diff_mean
    orderlist=sorted(unorderlist)
    if len(newdata[newdata.columns[i]])%2 != 0:
        median = int(round(len(newdata[newdata.columns[i]])/2))
        print "The median for %s is : %s"%(str(newdata.columns[i]),str(newdata[newdata.columns[i]][median])) 
    else:
        ran = int(round(len(newdata[newdata.columns[i]])/2))
        median = (newdata[newdata.columns[i]][ran] + newdata[newdata.columns[i]][ran+1])/2
        print "The median for %s is : %s"%(str(newdata.columns[i]),str(median))
    mode = max(set(orderlist), key=orderlist.count)
    print "The mode for %s is : %s"%(str(newdata.columns[i]),str(mode))
    ranges = (max(orderlist) - min(orderlist))
    print "The range for %s is : %s"%(str(newdata.columns[i]),str(ranges))
    variance = suming_variance/((len(newdata[newdata.columns[i]]))-1)
    print "The variance for %s is : %s"%(str(newdata.columns[i]),str(variance))
    stdev = (variance)**(1/2)
    print "The standard deviation for %s is : %s"%(str(newdata.columns[i]),str(stdev))
    print "----------------------------------END %s-------------------------------------------"%(str(newdata.columns[i]))
