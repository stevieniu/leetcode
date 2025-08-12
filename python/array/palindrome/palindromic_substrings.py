"""
647. Palindromic Substrings
https://leetcode.com/problems/palindromic-substrings/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.



Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand_from_mid(i, j):
            cnt = 0
            while i >= 0 and j < len(s):
                if s[i] == s[j]:
                    cnt += 1
                else:
                    break
                i -= 1
                j += 1
            return cnt

        ans = 0
        for i in range(len(s)):
            ans += expand_from_mid(i, i)
            if i < len(s) - 1:
                ans += expand_from_mid(i, i + 1)
        return ans