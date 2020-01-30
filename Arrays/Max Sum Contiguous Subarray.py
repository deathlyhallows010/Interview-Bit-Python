# https://www.interviewbit.com/problems/max-sum-contiguous-subarray/

# Max Sum Contiguous Subarray

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(A):
        i = 0;
        maxi = -1;
        index = 0;
        a = []

        while i < len(A):
            while i < len(A) and A[i] < 0:
                i+=1
            l = []
            index = i
            while i < len(A) and A[i] >= 0:   
                l.append(A[i])
                i+=1
        
            if (sum(l) > maxi):
                a = l
                maxi = sum(l)
        
        return a