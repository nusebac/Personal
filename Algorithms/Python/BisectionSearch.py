# -*- coding: utf-8 -*-
"""
@author: Arka
"""

enter = int(raw_input("Please enter a number : "))

error=0.01
low=0.0
high = enter
result=(low + high)/2.0

while abs(result**2 - enter) >= error:
    if result**2 < enter:
        low=result
    else:
        high =result
    result =(low + high)/2.0
print "Hey its near to the square root of %s"%(str(result))
