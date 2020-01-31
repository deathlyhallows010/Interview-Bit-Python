# https://www.interviewbit.com/problems/mathbug02/

# MATH_BUG02

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def squareSum(self,A):
        ans = []
        a = 1
        while a * a < A:
            b = 1
            while b * b < A:
                if a * a + b * b == A and b>=a:
                    newEntry = [a, b]
                    ans.append(newEntry)
                b += 1
            a += 1
        return ans
