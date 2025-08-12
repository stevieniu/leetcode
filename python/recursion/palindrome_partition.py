"""
131. Palindrome Partitioning
https://leetcode.com/problems/palindrome-partitioning/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.



Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]


Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.

"""


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s):
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        res = []

        def dfs(i, path):
            if i >= len(s):
                res.append(path.copy())
                return

            for j in range(i, len(s)):
                if isPalindrome(s[i: j + 1]):
                    path.append(s[i: j + 1])
                    dfs(j + 1, path)
                    path.pop()

        dfs(0, [])
        return res


