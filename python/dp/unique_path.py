"""
62. Unique Paths
https://leetcode.com/problems/unique-paths/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.



Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down


Constraints:

1 <= m, n <= 100
"""


class Solution:
    # def uniquePaths(self, m: int, n: int) -> int:
    #     dp = [[1] * n for _ in range(m)]
    #     for i in range(1, m):
    #         for j in range(1, n):
    #             dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    #     return dp[-1][-1]

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i == j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

#     def uniquePaths(self, m: int, n: int) -> int:
#         @lru_cache(None)
#         def dfs(i, j):
#             if i == j == 0:
#                 return 1
#             elif i < 0 or j < 0 or i == m or j == n:
#                 return 0
#             else:
#                 return dfs(i - 1, j) + dfs(i, j - 1)

#         return dfs(m - 1, n - 1)