# -*- coding: utf-8 -*-
"""
@author: Arka
"""
from __future__ import division
import pandas as pd

# Here I have given static file path and format.With panda we can manipulate that easily according to requirement

data = pd.ExcelFile("C:/Users/HP/Desktop/Book1.xlsx")
newdata=data.parse('Sheet1')

# Variables declaration
xsum=0
ysum=0
xysum=0
x2sum=0
y2sum=0
mx=0
b=0
N=0
input_feature = newdata[newdata.columns[0]]
target_var = newdata[newdata.columns[1]]

# xsum - The sum of all the values in the x column.
for val in input_feature:
    xsum += val

# ysum - The sum of all the values in the y column.
for vals in target_var:
    ysum += vals

# xysum - The sum of the products of the xn and yn that are recorded at the same time (vertical on this chart).
for i in range(len(newdata)):
    product = newdata.ix[i][0] * newdata.ix[i][1]
    xysum +=product

# x2sum - The total of each value in the x column squared and then added together.
for val1 in input_feature:
    x2sum += (val1**2)

# y2sum - The total of each value in the y column squared and then added together.
for vals1 in target_var:
    y2sum += (vals1**2)

# N - The total number of elements (or trials in your experiment).
N =len(newdata)

# The best form for our line is slope-intercept form, which looks like y = mx + b. Therefore, it is only necessary to compute m and b to determine the best fit line.Those values can be computed by the following equations
mx =((N*xysum)-(xsum*ysum))/((N*x2sum)-(xsum*xsum))
b =((x2sum*ysum)-(xsum*xysum))/((N*x2sum) -(xsum*xsum))

print "Equation of the line is y = %sx + %s"%(str(mx),str(b))
 
 
# The value of R-square to understand model fit.R is the correlation coefficient for univariate regression.

Rsquare = ((N*xysum - xsum*ysum)**2)/((N*x2sum - xsum*xsum)*(N*y2sum - ysum*ysum))
print "The value of Rsquare is : %s"%(str(Rsquare))


