"""
9. Palindrome Number
https://leetcode.com/problems/palindrome-number/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

Given an integer x, return true if x is a palindrome, and false otherwise.



Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


Constraints:

-231 <= x <= 231 - 1


Follow up: Could you solve it without converting the integer to a string?
"""


class Solution:
    # def isPalindrome(self, x: int) -> bool:
    #     if x < 0: return False

    #     if x % 10 == 0:
    #         return x == 0
    #     res = 0
    #     while res < x:
    #         digit = x % 10
    #         res = res * 10 + digit
    #         x //= 10

    #     print(res)
    #     print(x)
    #     return res == x or res // 10 == x

    # def isPalindrome(self, x: int) -> bool:
    #     if x < 0: return False
    #     # there is only 1 digit, it is palindrome
    #     if x // 10 == 0:
    #         return True
    #     div = 10 ** int(log10(x))
    #     while x and div:
    #         right = x % 10
    #         left = x // div
    #         if right != left:
    #             return False
    #         # chop off highest digit
    #         x %= div
    #         # chop off lowest digit
    #         x //= 10
    #         div //= 100
    #     return True

    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        if x // 10 == 0: return True
        div = 10 ** int(math.log10(x))
        while x and div:
            low = x % 10
            high = x // div
            if low != high:
                return False
            # chop off high
            x %= div
            # chop off low
            x //= 10
            div //= 100

        return True