# https://www.interviewbit.com/problems/set-matrix-zeros/

# Set Matrix Zeros

# Input 1:
#     [   [1, 0, 1],
#         [1, 1, 1], 
#         [1, 1, 1]   ]

# Output 1:
#     [   [0, 0, 0],
#         [1, 0, 1],
#         [1, 0, 1]   ]

# Input 2:
#     [   [1, 0, 1],
#         [1, 1, 1],
#         [1, 0, 1]   ]

# Output 2:
#     [   [0, 0, 0],
#         [1, 0, 1],
#         [0, 0, 0]   ]

class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(A):
        
        m = len(A[0])
        n = len(A)
        list_row = []
        list_col = []
        
        for i in range(n):
            for j in range(m):
                if A[i][j] == 0:
                    if i not in list_row:
                        list_row.append(i)
                    if j not in list_col:
                        list_col.append(j)
        #print list_row, list_col
        row = [0]*m
        
        for i in range(n):
            if i in list_row:
                A[i] = row
            for j in range(m):
                if j in list_col:
                    A[i][j] = 0
            
        return A