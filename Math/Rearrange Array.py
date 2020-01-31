# https://www.interviewbit.com/problems/rearrange-array/

# Rearrange Array

# Rearrange a given array so that Arr[i] becomes Arr[Arr[i]] with O(1) extra space.

class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference. 
    # You do not need to return anything in this case. 
    def arrange(self,A):
        n = len(A)
        for i in range(n):
            A[i] = A[i] + (A[A[i]]%n)*n
        
        for i in range(n):
            A[i] = A[i]//n
        return A
