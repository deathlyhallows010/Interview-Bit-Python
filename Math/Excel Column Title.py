# https://www.interviewbit.com/problems/excel-column-title/

# Excel Column Title

# Given a positive integer, return its corresponding column title as appear in an Excel sheet.

class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        mydict = 'ZABCDEFGHIJKLMNOPQRSTUVWXY'
        
        s = ''
        while A > 0:
            aux = A%26
            s = mydict[aux]+s
            A = A//26
            if 0 == aux:
                A -= 1
        
        return s