"""
29. Divide Two Integers
https://leetcode.com/problems/divide-two-integers/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.



Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.


Constraints:

-231 <= dividend, divisor <= 231 - 1
divisor != 0

"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        # Constants.
        MAX_INT = 2147483647  # 2**31 - 1
        MIN_INT = -2147483648  # -2**31
        HALF_MIN_INT = -1073741824  # MIN_INT // 2

        # Special case: overflow.
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        # We need to convert both numbers to negatives.
        # Also, we count the number of negatives signs.
        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = -dividend
        if divisor > 0:
            negatives -= 1
            divisor = -divisor

        # In the first loop, we simply find the largest double of divisor
        # that fits into the dividend.
        # The >= is because we're working in negatives. In essence, that
        # piece of code is checking that we're still nearer to 0 than we
        # are to INT_MIN.
        highest_double = divisor
        highest_power_of_two = -1
        while (
            highest_double >= HALF_MIN_INT
            and dividend <= highest_double + highest_double
        ):
            highest_power_of_two += highest_power_of_two
            highest_double += highest_double

        # In the second loop, we work out which powers of two fit in, by
        # halving highest_double and highest_power_of_two repeatedly.
        # We can do this using bit shifting so that we don't break the
        # rules of the question :-)
        quotient = 0
        while dividend <= divisor:
            if dividend <= highest_double:
                quotient += highest_power_of_two
                dividend -= highest_double
            # We know that these are always even, so no need to worry about the
            # annoying "bit-shift-odd-negative-number" case.
            highest_power_of_two >>= 1
            highest_double >>= 1

        # If there was originally one negative sign, then
        # the quotient remains negative. Otherwise, switch
        # it to positive.
        return quotient if negatives == 1 else -quotient