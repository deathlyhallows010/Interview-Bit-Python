# https://www.interviewbit.com/problems/all-factors/

# All Factors

import math   
def printDivisors(self,n) :
    l = []
    i = 1
    while i <= math.sqrt(n):
        if (n % i == 0) : 
            if (n / i == i) : 
                l.append(i)
            else : 
                l.append(i)
                l.append(int(n/i))
        i = i + 1
        l.sort()
    return l