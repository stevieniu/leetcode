"""
32. Longest Valid Parentheses
https://leetcode.com/problems/longest-valid-parentheses/description/?envType=company&envId=linkedin&favoriteSlug=linkedin-thirty-days

Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.



Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0


Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.
"""


class Solution:
    # def longestValidParentheses(self, s: str) -> int:
    #     if len(s) == 0:
    #         return 0
    #     dp = [0 ] * len(s)
    #     max_len = 0
    #     for i in range(len(s)):
    #         if s[i] == ')' and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
    #             dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
    #             max_len = max(max_len, dp[i])
    #     return max_len
    def longestValidParentheses(self, s: str) -> int:
        i = 0
        l_cnt = r_cnt = 0
        max_cnt = 0
        # from left to right
        while i < len(s):
            if s[i] == '(':
                l_cnt += 1
            else:
                r_cnt += 1

            if l_cnt == r_cnt:
                max_cnt = max(max_cnt, l_cnt + r_cnt)
            elif r_cnt > l_cnt:
                # )( => reset
                r_cnt = l_cnt = 0
            i += 1

        i = len(s) - 1
        r_cnt = l_cnt = 0
        # from right to left
        while i >= 0:
            if s[i] == '(':
                l_cnt += 1
            else:
                r_cnt += 1

            if l_cnt == r_cnt:
                max_cnt = max(max_cnt, l_cnt + r_cnt)
            elif r_cnt < l_cnt:
                # )( => reset
                r_cnt = l_cnt = 0
            i -= 1
        return max_cnt



