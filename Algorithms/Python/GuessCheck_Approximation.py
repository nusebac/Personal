# -*- coding: utf-8 -*-
"""
@author: Arka
"""
#Guess & Check Algorithm for integer values
enter = raw_input('Enter a Value : ')

if int(enter) > 0:
    for i in range(1,(int(enter) + 1)):
        if i**2 == int(enter):
            print "Hey its a sqaue root of :" +str(i)
            result = 1
        elif i**3 == int(enter):
            print "Hey its a cube root of :" + str(i)
            result = 1
    if result != 1:
        print "Its not a square root or cube root :"+str(enter)
else:
    enter = abs(int(enter))
    for j in range(1,(enter+1)):
        if j**2 == enter:
            print "Hey its a negative sqaue root of :" +str(j)
            result = 1
        elif j**3 == enter:
            print "Hey its a negative cube root of :" + str(j)
            result = 1
    if result != 1:
        print "Its not a square root or cube root :"+str(enter)
        
#Approximation Algorithm for floating point numbers
