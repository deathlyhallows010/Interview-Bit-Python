# https://www.interviewbit.com/problems/matrix-search/

# Matrix Search

# Given a matrix of integers A of size N x M and an integer B.
# Write an efficient algorithm that searches for integar B in matrix A.

class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        rows = len(A)
        for row in range(rows):
            start = 0
            end = len(A[row])-1
            while start <= end:
                mid = (start+end)//2
                if A[row][mid] == B:
                    return 1
                elif B < A[row][mid]:
                    end = mid-1
                else:
                    start = mid+1
        return 0