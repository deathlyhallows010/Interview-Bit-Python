# https://www.interviewbit.com/problems/rotated-sorted-array-search/

# Rotated Sorted Array Search

# Given an array of integers A of size N and an integer B.
# array A is rotated at some pivot unknown to you beforehand.
# You are given a target value B to search. If found in the array, return its index, otherwise return -1.
# You may assume no duplicate exists in the array.

def BinarySearch(A,target):
    start  = 0
    end =  len(A) - 1
    
    while(start<=end):
        mid = (start + end)//2
        if A[mid] == target:
            return mid
        elif A[mid]>target:
            end = mid -1
        else:
            start = mid + 1
            
    return -1

def findMin(A):
    start = 0
    end = len(A)-1
    N = len(A)
    while(start<=end):
        if A[start]<=A[end]:
            return start
        mid = (start + end)//2
        nxt = (mid+1)%N
        prev = (mid-1+N)%N
        if A[mid]<=A[nxt] and A[mid]<=A[prev]:
            return mid
        elif A[mid]<=A[end]:
            end = mid -1
        elif A[mid]>=A[end]:
            start = mid +1
    
    return -1

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def search(self,A,B):
        A = list(A)
        n = findMin(A)
        if n == -1:
            return -1
        d
        
        A.sort()
        return (BinarySearch(A,B)+n)%len(A)