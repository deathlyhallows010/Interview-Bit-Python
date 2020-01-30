# https://www.interviewbit.com/problems/maximum-absolute-difference/

# Maximum Absolute Difference
# |A[i] - A[j]| + |i - j|


# class Solution:
#     # @param A : list of integers
#     # @return an integer
#     def maxArr(self, A):
#         mabs = 0
#         for i in range(len(A)-1):
#             for j in range(i+1,len(A)):
#                 mabs = max(mabs, abs(A[i]-A[j])+abs(i-j))
                
#         return mabs

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, a):
        n = len(a)
        
        # 1: (A[j] - A[i]) + (j - i) = (A[j] + j) - (A[i] + i)
        # 2: (A[j] - A[i]) + (i - j) = (A[j] - j) - (A[i] - i)
        
        ap = [a[i] + i for i in range(n)]
        am = [a[i] - i for i in range(n)]
        return max(max(ap) - min(ap), max(am) - min(am))