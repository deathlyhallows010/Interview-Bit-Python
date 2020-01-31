# https://www.interviewbit.com/problems/prime-sum/

# Prime Sum

# Given an even number ( greater than 2 ), 
# return two prime numbers whose sum will be equal to given number.
# Input : 4
# Output: 2 + 2 = 4

import math
class Solution:
    def primesum(self, n):
        isprime = [1] * (n + 1)
        isprime[0] = 0
        isprime[1] = 0

        for i in range(2, int(math.sqrt(n)) + 1):
            if isprime[i]:
                for j in range(i * 2, n + 1, i):
                    isprime[j] = 0

        for i in range(2, n):
            if isprime[i] and isprime[n - i]:
                return [i, n - i]

        return []        