# https://www.interviewbit.com/problems/max-non-negative-subarray/

# Max Non Negative SubArray

# Input 1:
#     A = [1, 2, 5, -7, 2, 3]

# Output 1:
#     [1, 2, 5]

# Explanation 1:
#     The two sub-arrays are [1, 2, 5] [2, 3].
#     The answer is [1, 2, 5] as its sum is larger than [2, 3].

# Input 2:
#     A = [10, -1, 2, 3, -4, 100]
    
# Output 2:
#     [100]

# Explanation 2:
#     The three sub-arrays are [10], [2, 3], [100].
#     The answer is [100] as its sum is larger than the other two.

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