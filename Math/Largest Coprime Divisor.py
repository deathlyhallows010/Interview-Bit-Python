# https://www.interviewbit.com/problems/largest-coprime-divisor/

# Largest Coprime Divisor

# You are given two positive numbers A and B. You need to find the maximum valued integer X such that:
# 1. X divides A i.e. A % X = 0
# 2. X and B are co-prime i.e. gcd(X, B) = 1
    
def gcd(x, y):
    while(y):
        x, y = y, x%y
    return x

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def cpFact(self, x, y):
        
        while gcd(x,y)!=1:
            x = x//gcd(x,y)
        
        return x