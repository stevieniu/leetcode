"""
934. Shortest Bridge
https://leetcode.com/problems/shortest-bridge/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.



Example 1:

Input: grid = [[0,1],[1,0]]
Output: 1
Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1


Constraints:

n == grid.length == grid[i].length
2 <= n <= 100
grid[i][j] is either 0 or 1.
There are exactly two islands in grid.
"""

import collections
from typing import List
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        visit = set()

        def invalid(x, y):
            return x < 0 or x == n or y < 0 or y == n

        def bfs(x, y):
            res, q = 0, collections.deque(visit)

            while q:
                length = len(q)
                for i in range(length):
                    x, y = q.popleft()
                    for i, j in direction:
                        if invalid(x + i, y + j) or (x + i, y + j) in visit:
                            continue
                        if grid[x + i][y + j]:
                            return res
                        q.append((x + i, y + j))
                        visit.add((x + i, y + j))
                res += 1
            return res

        def dfs(x, y):
            if invalid(x, y) or not grid[x][y] or (x, y) in visit:
                return
            visit.add((x, y))

            for i, j in direction:
                dfs(x + i, y + j)

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    return bfs(i, j)



