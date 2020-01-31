# https://www.interviewbit.com/problems/binary-representation/

# Binary Representation

class Solution:
    # @param A : integer
    # @return a strings
    def findDigitsInBinary(self,n):
        
        if n==1 or n ==0:
            return n
        
        l = ''
        while(n>0):
            rem = n%2
            l += str(rem)
            n = int(n/2)

        return l[::-1]
        
