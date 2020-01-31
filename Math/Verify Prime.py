# https://www.interviewbit.com/problems/verify-prime/

# Verify Prime

import math
class Solution:
    # @param A : integer
    # @return an integer
    def isPrime(self,A):
        if A<=1:
            return 0
        
        if A>1:
            c=0
            for i in range(2,int(math.sqrt(A))+1):
                if A%i==0:
                    return 0
                                        
        return 1