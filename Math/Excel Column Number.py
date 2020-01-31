# https://www.interviewbit.com/problems/excel-column-number/

# Excel Column Number

# Given a column title as appears in an Excel sheet, return its corresponding column number.

class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        zip_ = zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', range(1,27))
        T = dict(zip_)
        sum_ = 0
        
        for i,j in enumerate(A[::-1]):
            sum_+=T[j]*(26**i)
                   
        return sum_