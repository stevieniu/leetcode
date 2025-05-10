"""
72. Edit Distance
https://leetcode.com/problems/edit-distance/description/

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character


Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')


Constraints:

0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.
"""

from functools import lru_cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(None)
        def dfs(i, j):  # miniDistance for word1[i:] and word2[j:]
            if i == len(word1):
                return len(word2) - j
            elif j == len(word2):
                return len(word1) - i

            if word1[i] == word2[j]:  # two characters are equal, no action needed, go to next index
                return dfs(i + 1, j + 1)

            return 1 + min(dfs(i + 1, j + 1), dfs(i + 1, j), dfs(i, j + 1))

        return dfs(0, 0)

    def minDistance(self, word1: str, word2: str) -> int:
        ROW, COL = len(word1), len(word2)
        dp = [[0] * (COL + 1) for _ in range(ROW + 1)]  # mini edit distance for word1[: i + 1] and word2[: j + 1]

        for i in range(ROW + 1):
            dp[i][0] = i

        for j in range(COL + 1):
            dp[0][j] = j

        for i in range(1, ROW + 1):
            for j in range(1, COL + 1):
                dp[i][j] = dp[i - 1][j - 1] if word1[i - 1] == word2[j - 1] else \
                    1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]
