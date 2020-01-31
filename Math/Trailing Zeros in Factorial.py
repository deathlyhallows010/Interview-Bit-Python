# https://www.interviewbit.com/problems/trailing-zeros-in-factorial/

# Trailing Zeros in Factorial

# Given an integer n, return the number of trailing zeroes in n

class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self,n):
        count  = 0
        num = 5
        while(n//num != 0):
            count += int(n/num)
            num  = num*5
        return int(count)