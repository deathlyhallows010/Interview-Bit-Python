# https://www.interviewbit.com/problems/maximum-unsorted-subarray/

# Maximum Unsorted Subarray

# Input 1:
# A = [1, 3, 2, 4, 5]
# Return: [1, 2]
# Input 2:
# A = [1, 2, 3, 4, 5]
# Return: [-1]

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        si = -1
        ei = 0
        max1 = 0
        min1 = max(A)
        minind = -1
        for i in range(1,len(A)):
            if A[i] < A[i - 1] or A[i] < max1:
                if si == -1:
                    si = i - 1
                ei = i
                min1 = min(min1,A[i])
            max1 = max(max1,A[i])
            
        if si == -1:
            return [-1]
        else:
            for i in range(0,si):
                if A[i] > min1:
                    minind = i
                    break
            if minind < si and minind != -1:
                si = minind
            return [si,ei]
        