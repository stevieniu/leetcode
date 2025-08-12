"""
1216. Valid Palindrome III
https://leetcode.com/problems/valid-palindrome-iii/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

Given a string s and an integer k, return true if s is a k-palindrome.

A string is k-palindrome if it can be transformed into a palindrome by removing at most k characters from it.



Example 1:

Input: s = "abcdeca", k = 2
Output: true
Explanation: Remove 'b' and 'e' characters.
Example 2:

Input: s = "abbababa", k = 1
Output: true


Constraints:

1 <= s.length <= 1000
s consists of only lowercase English letters.
1 <= k <= s.length
"""


class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        if not k:
            return is_palindrome(0, len(s) - 1)

        @lru_cache(None)
        def dfs(l, r, k):  # if s[l : r + 1] with k opertion left is palindrome?
            if not k:
                return is_palindrome(l, r)
            while l < r:
                if s[l] == s[r]:
                    return dfs(l + 1, r - 1, k)
                else:
                    return dfs(l + 1, r, k - 1) or dfs(l, r - 1, k - 1)
            return True

        return dfs(0, len(s) - 1, k)