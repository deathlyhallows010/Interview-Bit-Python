# https://www.interviewbit.com/problems/sum-of-pairwise-hamming-distance/

# Sum of pairwise Hamming Distance

# HammingDistance(2, 7) = 2, as only the first and 
# the third bit differs in the binary representation of 2 (010) and 7 (111).

def findDigitsInBinary(n):
        if n==1 or n ==0:
            return str(n)
        l = ''
        while(n>0):
            rem = n%2
            l = l + str(rem)
            n = int(n/2)
        return l[::-1]
    
def Diff(li1, li2):
    mx = max(len(li1),len(li2))
    li1  = '0'*(mx-len(li1)) + li1
    li2  = '0'*(mx-len(li2)) + li2
            
    total = 0
    for i in range(len(li1)):
        total = total + abs(int(li1[i]) - int(li2[i]))
    return total
        

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def hammingDistance(self,A):
        HamDist = 0
        arr = []
        for i in range(len(A)):
            for j in range(i,len(A)):
                if (i!=j):
                    HamDist = HamDist + Diff(findDigitsInBinary(A[i]),findDigitsInBinary(A[j]))                  
             
        return 2*HamDist

# class Solution:
#     # @param A : tuple of integers
#     # @return an integer
#     def hammingDistance(self,A):
#         bits = [0]*32;
#         digits = 0;
#         for num in A:
#             i = 0;
#             while num > 0:
#                 bits[i] += num%2;
#                 num= num//2;
#                 i+=1;
#             digits = max(i, digits);
#         ans = 0;
#         for i in range(digits):
#             ans += bits[i]*(len(A)-bits[i]);
#         return (2*ans)%1000000007;