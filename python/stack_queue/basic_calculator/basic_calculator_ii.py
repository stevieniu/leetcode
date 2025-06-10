"""
227. Basic Calculator II
https://leetcode.com/problems/basic-calculator-ii/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
Given a string s which represents an expression, evaluate this expression and return its value.

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().



Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5


Constraints:

1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.
"""

class Solution:
    def calculate(self, s: str) -> int:
        # 3+5 / 2
        #       i
        # cur =2, , res = 0,  operate = +
        # stack = [3, 2]
        cur, res = 0, 0
        operator = '+'
        stack = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                cur = int(s[i])
                while i < len(s) - 1 and s[i + 1].isdigit():
                    cur = 10 * cur + int(s[i + 1])
                    i += 1
            if not s[i].isdigit() and s[i] != ' ' or i == len(s) - 1:
                if operator == '+':
                    stack.append(cur)
                elif operator == '-':
                    stack.append(-cur)
                elif operator == '*':
                    stack.append(stack.pop() * cur)
                elif operator == '/':
                    stack.append(int(stack.pop() / cur))
                operator = s[i]
                cur = 0
            i += 1
        for num in stack:
            res += num
        return res
