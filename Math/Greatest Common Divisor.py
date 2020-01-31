# https://www.interviewbit.com/problems/greatest-common-divisor/

# Greatest Common Divisor

#Given 2 non negative integers m and n, find gcd(m, n)

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, x, y):
        while(y):
            x, y = y, x%y
        return x