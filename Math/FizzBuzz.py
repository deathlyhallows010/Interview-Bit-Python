# https://www.interviewbit.com/problems/fizzbuzz/

# FizzBuzz

# A = 5 , Return: [1 2 Fizz 4 Buzz]
# For numbers which are multiple of 3 and 5 both,
# the array should have “FizzBuzz” instead of the number.

class Solution:
    # @param A : integer
    # @return a list of strings
    def fizzBuzz(self, A):
        arr = []
        for i in range(1,A+1):
            if i%15 == 0:
                arr.append("FizzBuzz")
            elif i%3 == 0:
                arr.append("Fizz")
            elif i%5 == 0:
                arr.append("Buzz")
            else:
                arr.append(i)
        return arr