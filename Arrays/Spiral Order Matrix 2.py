# https://www.interviewbit.com/problems/spiral-order-matrix-ii/

# Spiral Order Matrix 2

# Input 1:
#     A = 3

# Output 1:
#     [   [ 1, 2, 3 ],
#         [ 8, 9, 4 ],
#         [ 7, 6, 5 ]   ]

import numpy as np # Used just for the generation of 2d Array
class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        
        B=np.ones((A,A),dtype=int)
        i,j=0,0
        T,D,L,R=0,A,0,A
        num=1
        while(T<D or L<R):
            for i in range(L,R):
                B[T][i]=num
                num+=1
            T+=1
            for i in range(T,D):
                B[i][R-1]=num
                num+=1
            R-=1
            for i in range(R-1,L-1,-1):
                B[D-1][i]=num
                
                num+=1
            D-=1
            for i in range(D-1,T-1,-1):
                B[i][L]=num
                num+=1
            L+=1
        return(B)