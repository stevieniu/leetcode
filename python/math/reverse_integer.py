"""
7. https://leetcode.com/problems/reverse-integer/description/

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21


Constraints:

-231 <= x <= 231 - 1
"""

import math
class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2 ** 31
        is_negative = x < 0

        if not is_negative: x = -x
        res = 0
        while int(x / 10):
            # -123
            res = res * 10 + int(math.fmod(x, 10))
            x = int(x / 10)

        if res < int(MIN / 10): return 0

        residule = int(math.fmod(x, 10))
        if res == int(MIN / 10) and not is_negative and residule >= 8:
            return 0
        elif res == int(MIN / 10) and is_negative and residule > 8:
            return 0
        else:
            res = 10 * res + residule
            return res if is_negative else -res




