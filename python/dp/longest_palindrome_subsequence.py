"""
516. Longest Palindromic Subsequence
https://leetcode.com/problems/longest-palindromic-subsequence/description/?envType=company&envId=linkedin&favoriteSlug=linkedin-three-months
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.



Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".


Constraints:

1 <= s.length <= 1000
s consists only of lowercase English letters.
"""

from functools import lru_cache
class Solution:
    # def longestPalindromeSubseq(self, s: str) -> int:
    #     dp = {}
    #     def dfs(i, j):
    #         if (i, j) in dp:
    #             return dp[(i, j)]

    #         if i < 0 or j == len(s):
    #             return 0

    #         if s[i] == s[j]:
    #             dp[(i, j)] = dfs(i - 1, j + 1) + (1 if i == j else 2 )
    #         else:
    #             dp[(i, j)] = max(dfs(i - 1, j), dfs(i, j + 1))
    #         return dp[(i, j)]
    #     res = 0
    #     for i in range(len(s)):
    #         res = max(res, dfs(i, i), dfs(i, i + 1))
    #     return res

    def longestPalindromeSubseq(self, s: str) -> int:
        @lru_cache(None)
        def dfs(i, j):
            if i > j:
                return 0
            if i == j:
                return 1

            if s[i] == s[j]:
                return dfs(i + 1, j - 1) + 2
            else:
                return max(dfs(i + 1, j), dfs(i, j - 1))

        return dfs(0, len(s) - 1)