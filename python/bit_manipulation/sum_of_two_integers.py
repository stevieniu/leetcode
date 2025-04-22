"""
371. Sum of Two Integers
https://leetcode.com/problems/sum-of-two-integers/description/

Given two integers a and b, return the sum of the two integers without using the operators + and -.



Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = 2, b = 3
Output: 5


Constraints:

-1000 <= a, b <= 1000

this should use Java, python doesn't work
"""
class Solution:
    def getSum(self, a: int, b: int) -> int:
         # a = 2, b = 3  a & b << 1 get the overall carry
          #  10 =>  1) 10 ^ 11 = 01
          #  11    10 & 11 = 10, 10 << 1 = 110 (this is the overall carry for 10 + 11)
           #         2) 110 + 01 => 110 ^ 01 = 111               => 111 ^ 0 = 111(5)
    #                            => 110 & 01 = 0, 0 << 1 = 0
         # -----
        #   1 0  1
        while b:
            tmp = (a & b) << 1 # ovarall carry
            a ^= b
            b = tmp
        return a


a = -1
b = 1
print(Solution().getSum(a, b))