# https://www.interviewbit.com/problems/palindrome-integer/

# Palindrome Integer

# Determine whether an integer is a palindrome. Do this without extra space.

class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, n):
        n = str(n)
        for i in range(int(len(n)/2)):
            if n[i] != n[len(n)-1-i]:
                return 0
        return 1