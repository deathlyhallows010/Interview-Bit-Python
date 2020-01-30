# https://www.interviewbit.com/problems/maximum-consecutive-gap/

# Maximum Consecutive Gap

# Input : [1, 10, 5]
# Output : 5 

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        if len(A) == 1:
            return 0
        A=sorted(A)
        diff = 0
        for i in range(len(A)-1):
            diff = max(diff, A[i+1]-A[i])
        return diff