# https://www.interviewbit.com/problems/sorted-insert-position/

# Sorted Insert Position

# Given a sorted array and a target value,
# return the index if the target is found. If not,
# return the index where it would be if it were inserted in order.

# [1,3,5,6], 5 → 2
# [1,3,5,6], 2 → 1
# [1,3,5,6], 7 → 4
# [1,3,5,6], 0 → 0


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        start = 0
        end = len(A)

        while(start<end):
            mid = (start+end)//2
            if A[mid]<B:
                start = mid + 1
            else:
                end = mid
        
        return start