# https://www.interviewbit.com/problems/power-of-two-integers/

# Power Of Two Integers

# Given a positive integer which fits in a 32 bit signed integer, 
# find if it can be expressed as A^P where P > 1 and A > 0. A and P both should be integers.

from math import log, sqrt
class Solution:
    # @param A : integer
    # @return an integer
    def isPower(self, A):
        if A==1:
            return 1
        
        for i in range(2,int(sqrt(A))+1):
            x=round(log(A,i),5)
            if x%1==0:
                return 1
                
        return 0