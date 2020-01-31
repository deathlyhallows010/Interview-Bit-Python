# https://www.interviewbit.com/problems/count-element-occurence/

# Count Element Occurence

# Given a sorted array of integers, find the number of occurrences of a given target value.
# Your algorithm’s runtime complexity must be in the order of O(log n).
# If the target is not found in the array, return 0

def FirstOccurance(A,target):
    start  = 0
    end =  len(A) - 1
    result = -1
    
    while(start<=end):
        mid = (start + end)//2
        if A[mid] == target:
            result = mid
            end =  mid - 1
        elif A[mid]>target:
            end = mid -1
        else:
            start =  mid + 1
            
    return result

def LastOccurance(A,target):
    start  = 0
    end =  len(A) - 1
    result = -1
    
    while(start<=end):
        mid = (start + end)//2
        if A[mid] == target:
            result = mid
            start = mid +1
        elif A[mid]>target:
            end = mid -1
        else:
            start =  mid + 1
            
    return result

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def findCount(self, A, B):
        first = FirstOccurance(A,B)
        last = LastOccurance(A,B)
        if first == -1:
            return [-1,-1]
        return last-first+1