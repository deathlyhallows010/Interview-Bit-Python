# https://www.interviewbit.com/problems/next-permutation/

# Next Permutation

# Input  1: A = [1, 2, 3] 
# Output 1:     [1, 3, 2] 
# Input  2: A = [3, 2, 1]
# Output 2:     [1, 2, 3]
# Input  3: A = [1, 1, 5]
# Output 3:     [1, 5, 1]
# Input  4: A = [20, 50, 113]
# Output 4:     [20, 113, 50]

def next_permutation(arr):
    n = len(arr)
    i = n - 2
    while i >= 0 and arr[i] >= arr[i+1]:
        i -= 1
    if i == -1:
        return False
    j = i + 1
    while j < n and arr[j] > arr[i]:
        j += 1
    j -= 1
    arr[i], arr[j] = arr[j], arr[i]
    left = i + 1
    right = n - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return True
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextPermutation(self, A):
        if not next_permutation(A):
            A.sort()
            return A
        return A
