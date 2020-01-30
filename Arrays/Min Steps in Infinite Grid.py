# https://www.interviewbit.com/problems/min-steps-in-infinite-grid/

# Min Steps in Infinite Grid

def minDistance(A,B):
    steps = 0
    for i in range(len(A)-1):
        x = abs(A[i]-A[i+1])
        y = abs(B[i]-B[i+1])
        
        steps += max(x,y)
    return steps