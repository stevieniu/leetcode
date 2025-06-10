"""
65. https://leetcode.com/problems/valid-number/description/?envType=study-plan-v2&envId=programming-skills

Given a string s, return whether s is a valid number.

For example, all the following are valid numbers: "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789", while the following are not valid numbers: "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53".

Formally, a valid number is defined using one of the following definitions:

An integer number followed by an optional exponent.
A decimal number followed by an optional exponent.
An integer number is defined with an optional sign '-' or '+' followed by digits.

A decimal number is defined with an optional sign '-' or '+' followed by one of the following definitions:

Digits followed by a dot '.'.
Digits followed by a dot '.' followed by digits.
A dot '.' followed by digits.
An exponent is defined with an exponent notation 'e' or 'E' followed by an integer number.

The digits are defined as one or more digits.



Example 1:

Input: s = "0"

Output: true

Example 2:

Input: s = "e"

Output: false

Example 3:

Input: s = "."

Output: false



Constraints:

1 <= s.length <= 20
s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'.
"""
class Solution:
    class Solution:
        def isNumber(self, s: str) -> bool:
            seen_digit, seen_exp, seen_dot = False, False, False
            for i, c in enumerate(s):
                if c.isdigit():
                    seen_digit = True
                elif c in '+-':
                    # sign must be the first index, or right after e/E
                    if i > 0 and s[i - 1] not in 'Ee': return False  # 12e-1
                elif c == '.':
                    # 1). first index .1 , 2) right after digit 1. 3)cannot be after e/E 12E2.1 x
                    # 4) there is only 1 dot
                    if seen_dot or seen_exp: return False
                    seen_dot = True
                elif c in 'Ee':  # 1) cannot be the first index, must be after digit 2) there is only one E/e
                    if seen_exp or not seen_digit: return False
                    seen_exp = True
                    seen_digit = False  # in case e/E is the last index, this is not allowed
                else:
                    return False
            return seen_digit