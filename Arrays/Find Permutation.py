# https://www.interviewbit.com/problems/find-permutation/

# Find Permutation

# Given a positive integer n and a string s consisting only of letters D or I, 
# you have to find any permutation of first n positive integer that satisfy the given input string.

# Input 1:
# n = 3
# s = ID
# Return: [1, 3, 2]

class Solution:
    # @param A : string
    # @param B : integer
    # @return a list of integers
    def findPerm(self, s, n):
        mini = 1
        maxi = n
        result = []
        
        for x in s:
            if x == 'D':
                result.append(maxi)
                maxi -= 1
            elif x == 'I':
                result.append(mini)
                mini += 1
       
        result.append(mini)
        return result