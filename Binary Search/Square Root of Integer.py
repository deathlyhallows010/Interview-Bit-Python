# https://www.interviewbit.com/problems/square-root-of-integer/

# Square Root of Integer

# Given an integar A.
# Compute and return the square root of A.
# ,If A is not a perfect square, return floor(sqrt(A)

class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        
        if A==0 or A==1:
            return A
        
        start = 0
        end = A
        
        while(start<=end):
            mid = int((start + end)/2)
            if (mid*mid <= A):
                start = mid + 1;
                ans = mid
            else:
                end = mid - 1;
            
        return ans