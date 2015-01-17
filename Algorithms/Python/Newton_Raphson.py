# -*- coding: utf-8 -*-
"""
Created on Sun Jan 18 01:47:59 2015

@author: HP
"""
# Newton-Raphson for finding roots

enter =int(raw_input("Enter a value : "))

error=0.01
result = enter/2.0
while (abs(result*result) - enter) > error:
    result =result - ((result**2)-enter) /(2*result)

print "The square root is near to : %s"%(str(result))
