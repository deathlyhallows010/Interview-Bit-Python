# https://www.interviewbit.com/problems/repeat-and-missing-number-array/

# Repeat and Missing Number Array
# Input:[3 1 2 5 3] Output:[3, 4]  A = 3, B = 4

class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, arr):
        repeated =0
        missing =0
        aux = [-1]*len(arr)
        
        for item in arr:
            if aux[item-1]==1:
                repeated = item
                break
            else:
                aux[item-1]=1
        
        n = len(arr)
        missing = int((n*(n+1)/2)-sum(arr)+repeated)   # Using summation property to find the missing (Nice)
        return [repeated,missing]