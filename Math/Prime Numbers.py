# https://www.interviewbit.com/problems/prime-numbers/

# Prime Numbers

class Solution:
    # @param A : integer
    # @return a list of integers
    def sieve(self,A):
        prime  = [1] * A
        prime[0] = 0
        prime[1] = 0
        for i in range(2,A):
            if prime[i] == 1:
                j = 2
                while(i*j<A):
                    if i*j<A:
                        prime[i*j] = 0   # Multiples of i are set to zeros
                    j += 1
                    
        a  = []
        for i in range(len(prime)):
            if prime[i] == 1:
                a.append(i)
                
        return a
