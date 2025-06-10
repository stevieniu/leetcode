"""
224. Basic Calculator
https://leetcode.com/problems/basic-calculator/description/
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().



Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23


Constraints:

1 <= s.length <= 3 * 105
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
'+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
'-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
There will be no two consecutive operators in the input.
Every number and running calculation will fit in a signed 32-bit integer.
"""


class Solution:
    def calculate(self, s: str) -> int:
        res, cur, sign = 0, 0, 1  # res: calculated result so far. cur: current number; sign: 1-> +. -1 -> -
        stack = []
        # .                  i
        # (1+(4+5+2)-3)+(6+8)
        # [] cur = 0 , res += sign * cur = 23, sign = +
        #
        # c is digit => caluculate cur
        # c == ( => push 1) res to stack, 2) push sign to stack, 3) reset cur/res/sign
        # c == '+-' => 1) res += sign * cur 2) assign sign 3) reset cur
        # c == ) =? 1) res += sign * cur 2) pop sign, res += sign + res 3) pop previous res, res += Prevres, 4) reset cur
        # out of loop, calucalte rest => res += cur * sign
        for c in s:
            if c.isdigit():
                cur = 10 * cur + int(c)
            elif c == ')':
                res += sign * cur
                res *= stack.pop()  # this pop is previous sign stored in stack
                res += stack.pop()  # this pop is previous result stored in stack
                cur = 0
            elif c in '+-':
                res += cur * sign
                cur = 0
                sign = 1 if c == '+' else -1
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                cur, res, sign = 0, 0, 1
        return res + sign * cur

