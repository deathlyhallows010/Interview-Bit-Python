# https://www.interviewbit.com/problems/add-one-to-number/

# Add One To Number

# class Solution:
#     # @param A : list of integers
#     # @return a list of integers
#     def plusOne(self, A):
#         s = ''
#         for i in range(len(A)):
#             s += str(A[i])
            
#         val = int(s) + 1
#         val = list(str(val))
        
#         return [int(x) for x in val]

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        val = 1;
        for i in range(len(A),0,-1):
            val = val + A[i-1]
            borrow = int(val/10)
            if borrow == 0:
                A[i-1] = val
                break;
            else:
                A[i-1] = val%10
                val = borrow
        A = [borrow] + A         ## Adding an element in front of an array
        while A[0]==0:
            del A[0]
        return A