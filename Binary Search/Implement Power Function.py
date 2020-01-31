# https://www.interviewbit.com/problems/implement-power-function/

# Implement Power Function

# Implement pow(x, n) % d.

# def Power(x,n):
#     if n == 0:
#         return 1
#     if n%2 == 0:
#         y = Power(x,n/2)
#         return y*y
#     else:
#         return x*Power(x,n-1)

class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        if n==0:
            return 1
        if n%2 == 0:
            y = pow(x,n/2,d)
            return ((y%d)*(y%d))%d
        else:
            return ((x%d)*(pow(x,n-1,d)))%d
                