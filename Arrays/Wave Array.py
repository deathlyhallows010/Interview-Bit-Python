# https://www.interviewbit.com/problems/wave-array/

# Wave Array

# Given [1, 2, 3, 4]
# One possible answer : [2, 1, 4, 3]
# Another possible answer : [4, 1, 3, 2]

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        A.sort()
        i = 0
        while i<len(A)-1:
            A[i], A[i+1] = A[i+1], A[i]
            i = i + 2
        return A