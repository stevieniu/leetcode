"""
10. Regular Expression Matching
https://leetcode.com/problems/regular-expression-matching/description/

Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).



Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".


Constraints:

1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}
        # @lru_cache(maxsize=None)
        # def dfs(i, j):
        #     if (i, j) in cache:
        #         return cache[(i, j)]
        #     if i >= len(s) and j >= len(p):
        #         return True
        #     if j >= len(p):
        #         return False

        #     match = i < len(s) and (s[i] == p[j] or p[j] == '.')

        #     # p[j + 1] == *
        #     if (j + 1) < len(p) and p[j + 1] == '*':
        #         cache[(i, j)] = dfs(i, j + 2) or (match and dfs(i + 1, j))
        #         return cache[(i, j)]

        #     if match:
        #         cache[(i, j)] = dfs(i + 1, j + 1)
        #         return cache[(i, j)]
        #     return False
        # return dfs(0, 0)

    # def isMatch(self, s: str, p: str) -> bool:
    #     def dfs(i, j): # i index of s, j index of p
    #         if i >= len(s) and j >= len(p):
    #             return True
    #         if j >= len(p):
    #             return False
    #         # for case i >= len(s) only, cannot tell if match or not

    #         match = i < len(s) and (s[i] == p[j] or p[j] == '.')
    #         if j + 1 < len(p) and p[j + 1] == '*':
    #             return match and dfs(i + 1, j) or dfs(i, j + 2)
    #         if match:
    #             return dfs(i + 1, j + 1)
    #         return False
    #     return dfs(0, 0)

    def isMatch(self, s: str, p: str) -> bool:
        if len(p) == 0: return len(s) == 0
        first_match = len(s) > 0 and (s[0] == p[0] or p[0] == '.')
        if len(p) >= 2 and p[1] == '*':
            return first_match and self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
        else:
            return first_match and self.isMatch(s[1:], p[1:])