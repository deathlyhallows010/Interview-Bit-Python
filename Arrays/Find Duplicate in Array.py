# https://www.interviewbit.com/problems/find-duplicate-in-array/

# Find Duplicate in Array

# Input:[3 4 1 4 1] Output:1

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        dict = {}
        for i in range(len(A)):
            if A[i] not in dict:
                dict[A[i]] = 1
            else:
                return A[i]

# class Solution:
#     # @param A : tuple of integers
#     # @return an integer
#     def repeatedNumber(self, A):
#         size = len(A)
#         tmpList = [False]*(size)
#         for i in range(size):
#             if tmpList[int(A[i])]==True:
#                 return A[i]
#             else:
#                 tmpList[int(A[i])] = True
#         return -1