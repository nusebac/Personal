# -*- coding: utf-8 -*-
"""
@author: Arka
"""
#Guess & Check Algorithm for integer values
num = raw_input('Enter a Value : ')

def Guess_Check(enter):
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
def approx(enter):
    error =0.01
    step = error**2
    step1 = error**3
    ans=0.0
    ans1=0.0
    while (abs(ans**2-int(enter))) >= error and ans < int(enter):
        ans+=step
    
    if (abs(ans**2-int(enter))) >= error:
        print "Its not near to a perfect square root:"+str(ans) 
    else:
        print "Hey its near to the square root of:"+str(ans)
    while (abs(ans1**3-int(enter))) >= error and ans < int(enter):
        ans1+=step1
    
    if (abs(ans1**3-int(enter))) >= error:
        print "Its not near to a perfect square root:"+str(ans1) 
    else:
        print "Hey its also near to the cube root of:"+str(ans1)
        
try:
    Guess_Check(int(num))
except:
    approx(float(num))
