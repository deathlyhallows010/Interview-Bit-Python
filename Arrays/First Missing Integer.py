# https://www.interviewbit.com/problems/first-missing-integer/

# First Missing Integer

# Given an unsorted integer array, find the first missing positive integer.
# Example:
# Given [1,2,0] return 3,
# [3,4,-1,1] return 2,
# [-8, -7, -6] returns 1

class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        A.sort()
        n = len(A)
        i = 0
        j = 1
        while (i<n):
            if A[i]<=0:
                i+=1
                continue
            if A[i] != j:
                return j
            elif i == n - 1:
                return j + 1 
            else:
                i += 1
                j += 1
                
        return 1