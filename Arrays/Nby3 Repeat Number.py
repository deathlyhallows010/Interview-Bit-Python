# https://www.interviewbit.com/problems/n3-repeat-number/

# N/3 Repeat Number

# Input : [1 2 3 1 1]
# Output : 1 
# 1 occurs 3 times which is more than 5/3 times.

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(A):
        n = len(A)
        l = n / 3
        
        maj1 = 0
        maj2 = 0
        first = float('inf')
        second = float('inf') 
      
        for i in range(n):
            if first == A[i]: 
                maj1 += 1
            elif second == A[i]: 
                maj2 += 1
            elif maj1 == 0: 
                maj1 += 1
                first = A[i]
            elif maj2 == 0: 
                maj2 += 1
                second = A[i]
            else: 
                maj1 -= 1
                maj2 -= 1
        
        maj1 = 0
        maj2 = 0
        
        for i in range(n):  
            if A[i] == first: 
                maj1 += 1
            elif A[i] == second: 
                maj2 += 1
        
        if (maj1 > l): 
            return first
        if (maj2 > l): 
            return second
        return -1