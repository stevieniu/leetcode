"""
256. Paint House
There is a row of n houses, where each house can be painted one of three colors: red, blue, or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by an n x 3 cost matrix costs.

For example, costs[0][0] is the cost of painting house 0 with the color red; costs[1][2] is the cost of painting house 1 with color green, and so on...
Return the minimum cost to paint all houses.



Example 1:

Input: costs = [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
Minimum cost: 2 + 5 + 3 = 10.
Example 2:

Input: costs = [[7,6,2]]
Output: 2


Constraints:

costs.length == n
costs[i].length == 3
1 <= n <= 100
1 <= costs[i][j] <= 20
"""
from functools import lru_cache
from typing import List

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        N = len(costs)

        @lru_cache(None)
        def dfs(i, prev_color):
            """
            :param i: current house index
            :param prev_color:  paint color of house i -1
            :return: house i - 1 painted with prev_color, what is the minimum cost of house i to paint
            """
            if i == N:
                return 0

            res = float('inf')
            for curr_color in range(3):  # color value from 0 to 2
                if curr_color == prev_color: continue
                res = min(res, dfs(i + 1, curr_color) + costs[i][curr_color])
            return res

        return dfs(0, -1)

    def minCost(self, costs: List[List[int]]) -> int:
        N = len(costs)
        dp = [[float('inf')] * 3 for _ in range(N)]  # dp[i] is the mini cost to paint house i
        for color in range(3):
            dp[0][color] = costs[0][color]

        for i in range(1, N):
            for color in range(3):
                for prev_color in range(3):
                    if color == prev_color: continue
                    dp[i][color] = min(dp[i][color], dp[i - 1][prev_color] + costs[i][color])
        return min(dp[-1])

