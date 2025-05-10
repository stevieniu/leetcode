"""
265. Paint House II
https://leetcode.com/problems/paint-house-ii/description/
There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by an n x k cost matrix costs.

For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on...
Return the minimum cost to paint all houses.



Example 1:

Input: costs = [[1,5,3],[2,9,4]]
Output: 5
Explanation:
Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5;
Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5.
Example 2:

Input: costs = [[1,3],[2,4]]
Output: 5


Constraints:

costs.length == n
costs[i].length == k
1 <= n <= 100
2 <= k <= 20
1 <= costs[i][j] <= 20


Follow up: Could you solve it in O(nk) runtime?
"""


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n, k = len(costs), len(costs[0])

        @lru_cache(None)
        def dfs(i, prev_color):
            if i == n:
                return 0

            res = float('inf')
            for color in range(k):
                if color == prev_color:
                    continue
                res = min(res, dfs(i + 1, color) + costs[i][color])
            return res

        return dfs(0, -1)

    # def minCostII(self, costs: List[List[int]]) -> int:
    #     n, k = len(costs), len(costs[0])
    #     dp = [[float('inf') for _ in range(k)] for _ in range(n)]
    #     for l in range(k):
    #         dp[0][l] = costs[0][l]

    #     for i in range(1, n):
    #         for j in range(k):
    #             if j == 0:
    #                 dp[i][j] = costs[i][j] + min(dp[i - 1][1:])
    #             elif j == k - 1:
    #                 dp[i][j] = costs[i][j] + min(dp[i - 1][:-1])
    #             else:
    #                 dp[i][j] = costs[i][j] + min(dp[i - 1][:j] + dp[i - 1][j + 1:])
    #     return min(dp[-1])
    def minCostII(self, costs: List[List[int]]) -> int:
        n, k = len(costs), len(costs[0])
        dp = [[float('inf')] * k for _ in range(n)]  # dp[i][color] : minimum cost of house i paint with color
        for color in range(k):
            dp[0][color] = costs[0][color]

        for i in range(1, n):
            for color in range(k):
                for prev_color in range(k):
                    if color == prev_color: continue  # can't paint with the same color with last house
                    dp[i][color] = min(dp[i][color], dp[i - 1][prev_color] + costs[i][color])
        return min(dp[-1])

    def minCostII(self, costs: List[List[int]]) -> int:
        """
            c0 c1 c2
        h0: 1  5  3
        h1: 2  9  4
        """
        n, k = len(costs), len(costs[0])
        dp = [[float('inf')] * k for _ in range(n)]  # dp[i][color] : minimum cost of house i paint with color
        for color in range(k):
            dp[0][color] = costs[0][color]

        min_stack = []  # (cost, color) store the mini cost  and second mini cost (second) for one house
        for color, cost in enumerate(costs[0]):
            heapq.heappush(min_stack, (cost, color))
        prev_min_cost, prev_min_cost_color = heapq.heappop(min_stack)
        prev_second_min_cost = heapq.heappop(min_stack)[0]

        for i in range(1, n):  # iterate over house index
            min_stack = []
            for color, cost in enumerate(costs[i]):
                if color != prev_min_cost_color:
                    curr_cost = prev_min_cost + cost
                else:
                    curr_cost = prev_second_min_cost + cost
                heapq.heappush(min_stack, (curr_cost, color))
            min_cost, min_cost_color = heapq.heappop(min_stack)
            second_min_cost = heapq.heappop(min_stack)[0]
            prev_min_cost = min_cost
            prev_min_cost_color = min_cost_color
            prev_second_min_cost = second_min_cost
        return prev_min_cost
