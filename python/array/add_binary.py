"""
67. Add Binary
https://leetcode.com/problems/add-binary/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

Given two binary strings a and b, return their sum as a binary string.



Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.

"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 0123
        # 1010
        #   11
        #   01
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        ans = ''
        while i >= 0 or j >= 0 or carry:
            if i >= 0 and j >= 0:
                digit = int(a[i]) + int(b[j]) + carry
                carry = digit // 2
                digit %= 2
                i -= 1
                j -= 1
            elif i >= 0:
                digit = int(a[i]) + carry
                carry = digit // 2
                digit %= 2
                i -= 1
            elif j >= 0:
                digit = int(b[j]) + carry
                carry = digit // 2
                digit %= 2
                j -= 1
            else:
                digit = carry
                carry = digit // 2
                digit %= 2
            ans = str(digit) + ans
        return ans