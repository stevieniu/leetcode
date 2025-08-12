"""
5. https://leetcode.com/problems/longest-palindromic-substring/description/

Given a string s, return the longest palindromic substring in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.

"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_from_mid(l, r) -> (int, int):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return [l + 1, r - 1]

        maxx = 0
        n = len(s)
        ans = ''
        for i in range(n):
            [l1, r1] = expand_from_mid(i, i)
            if maxx < r1 - l1 + 1:
                ans = s[l1: r1 + 1]
                maxx = r1 - l1 + 1
            if i < n - 1:
                [l2, r2] = expand_from_mid(i, i + 1)
                if maxx < r2 - l2 + 1:
                    ans = s[l2: r2 + 1]
                    maxx = r2 - l2 + 1
        return ans


