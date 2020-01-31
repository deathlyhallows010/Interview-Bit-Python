# https://www.interviewbit.com/problems/rotated-array/

# Rotated Array

# Suppose a sorted array A is rotated at some pivot unknown to you beforehand.
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# How many times the array is rotated.

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def findMin(self, A):
        start = 0
        end = len(A)-1
        N = len(A)
        while(start<=end):
            if A[start]<=A[end]:
                return A[start]
            mid = (start + end)//2
            nxt = (mid+1)%N
            prev = (mid-1+N)%N
            if A[mid]<=A[nxt] and A[mid]<=A[prev]:
                return A[mid]
            elif A[mid]<=A[end]:
                end = mid -1
            elif A[mid]>=A[end]:
                start = mid +1
    
        return -1