# https://www.interviewbit.com/problems/sorted-permutation-rank/

# Sorted Permutation Rank

# Given a string, find the rank of the string amongst its permutations sorted lexicographically.
# Assume that no characters are repeated.

def fact (n ) :
    if n <= 1 :
        return 1
    else :
        return n * fact(n-1)


class Solution:
    # @param A : string
    # @return an integer

    def findRank(self, A):
        n = len(A)
        res = 1
        for i in range(0, n-1) :
            rank = 0
            for j in range(i+1, n) :
                if A[i] > A[j] :
                    rank += 1
            res = (res + rank * fact(n-i- 1))
        return res%1000003