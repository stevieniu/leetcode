"""
415. Add Strings
https://leetcode.com/problems/add-strings/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.



Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"


Constraints:

1 <= num1.length, num2.length <= 104
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.

"""
import collections
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        i, j = len(num1) - 1, len(num2) - 1
        q = collections.deque([])
        while i >= 0 or j >= 0 or carry == 1:
            if i >= 0 and j >= 0:
                cur_sum = int(num1[i]) + int(num2[j]) + carry
                q.appendleft(cur_sum % 10)
                carry = cur_sum // 10
                i -= 1
                j -= 1
            elif i >= 0:
                cur_sum = int(num1[i]) + carry
                q.appendleft(cur_sum % 10)
                carry = cur_sum // 10
                i -= 1
            elif j >= 0:
                cur_sum = int(num2[j]) + carry
                q.appendleft(cur_sum % 10)
                carry = cur_sum // 10
                j -= 1
            else:
                cur_sum = int(carry)
                q.appendleft(cur_sum % 10)
                carry = 0
        return ''.join(list(map(str, q)))