# https://www.interviewbit.com/problems/median-of-array/

# Median of Array

# There are two sorted arrays A and B of size m and n respectively.
# Find the median of the two sorted arrays ( The median of the array formed by merging both the arrays ).
# The overall run time complexity should be O(log (m+n)).


def Med(A):
    mid = len(A)//2
        
    if mid%2==0:
        return (A[mid-1]+A[mid])/2
    else:
        return A[mid]
    

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):
        
        A = list(A)
        B = list(B)
        
        if len(A)==0 or len(B)==0:
            C = A+B
            if len(C) == 1:
                return C[0]
            else:
                return Med(C)
       
        return (Med(A)+Med(B))/2
