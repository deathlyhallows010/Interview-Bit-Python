# https://www.interviewbit.com/problems/kth-row-of-pascals-triangle/

# Kth Row of a pascal's triangle
#  NOTE : k is 0 based. k = 0, corresponds to the row [1].

class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        if A <= 0:
            return [1]
        result = [[1]]
        for r in range(1, A+1):
            row = [1]
            for i in range(1,r):
                row.append(result[r-1][i-1] + result[r-1][i])
            row.append(1)
            result.append(row)
        return row
