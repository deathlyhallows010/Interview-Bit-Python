# https://www.interviewbitcom/problems/grid-unique-paths/

# Grid Unique Path

# Input : A = 2, B = 2
# Output : 2
# 2 possible routes : (0, 0) -> (0, 1) -> (1, 1) 
#               OR  : (0, 0) -> (1, 0) -> (1, 1)


class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self,rows, cols):
        
        if rows==1 or cols == 1:
            return 1
       
        a = [[1] + [0]*(cols-1)]*rows
        a[0] = [1]*cols
            
        for i in range(1,rows):
            for j in range(1,cols):
                a[i][j] = a[i-1][j] + a[i][j-1]

                
        
        return a[rows-1][cols-1]
