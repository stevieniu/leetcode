"""
322. Coin Change
https://leetcode.com/problems/coin-change/description/

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.



Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0


Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
"""
from typing import List
from functools import lru_cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1) # dp[i]: mini number of coins to respent amount i
        dp[0] = 0
        for amt in range(1, len(dp)):
            for c in coins:
                if amt >= c:
                    dp[amt] = min(dp[amt], 1 + dp[amt - c])
        return -1 if dp[-1] == float('inf') else dp[-1]

    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def dfs(amount):  # fewest number of coins that you need to make up that amount
            if amount == 0:  # 0 way to make up to 0, base case
                return 0
            elif amount < 0:  # no way to make up
                return -1

            ans = float('inf')
            for coin in coins:
                number = dfs(amount - coin)
                if number != -1:
                    ans = min(ans, 1 + number)
            return ans if ans != float('inf') else -1

        return dfs(amount)