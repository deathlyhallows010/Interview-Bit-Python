# https://www.interviewbit.com/problems/reverse-integer/

# Reverse integer

# Reverse digits of an integer

class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self,A):
        sign = -1 if A < 0 else 1
        A = abs(A)
        string = str(A)
        reverse = string[::-1]
        result = int(reverse)
        if result > 2**31 - 1:
            return 0
        return sign * result