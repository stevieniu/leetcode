"""
70. Climbing Stairs
https://leetcode.com/problems/climbing-stairs/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:

1 <= n <= 45
"""

from functools import lru_cache
class Solution:
    # bottom up
    # def climbStairs(self, n):
    #     if n == 1:
    #         return 1

    #     step = 0
    #     s0, s1 = 1, 1
    #     for i in range(2, n + 1):
    #         step = s0 + s1
    #         s0, s1 = s1, step
    #     return step

    # top down
    def climbStairs(self, n):
        @lru_cache(None)
        def dfs(i):
            if i == 0 or i == 1:
                return 1

            return dfs(i - 1) + dfs(i - 2)

        return dfs(n)

    def climbStairs(self, n):
        dp = [1] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

