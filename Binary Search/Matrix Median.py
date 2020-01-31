# https://www.interviewbit.com/problems/matrix-median/

# Matrix Median

# Given a matrix of integers A of size N x M in which each row is sorted.
# Find an return the overall median of the matrix A.

# class Solution:
#     # @param A : list of list of integers
#     # @return an integer
#     def findMedian(self, A):    
#         if len(A)==0:
#             return []     
#         arr = []
#         for row in A:
#             arr.extend(row) 
#         arr = sorted(arr)
#         median_index = (len(arr)+1)//2
#         return arr[median_index-1]

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def findMedian(self, A):
        def arr_median(arr):
            arr = sorted(arr)
            median_index = (len(arr)+1)//2
            return arr[median_index-1]
            
        if len(A)==0:
            return []
        
        arr = []
        for row in A:
            arr.extend(row) 
        
        return arr_median(arr)