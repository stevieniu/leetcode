"""
695. Max Area of Island
https://leetcode.com/problems/max-area-of-island/description/?envType=company&envId=linkedin&favoriteSlug=linkedin-three-months

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.



Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
"""

from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def dfs(x, y):
            if x < 0 or x == m or y < 0 or y == n or grid[x][y] == 0:
                return 0
            area = 0
            for r, c in direction:
                grid[x][y] = 0
                area += dfs(x + r, y + c)
            return area + 1

        maxArea = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = dfs(i, j)
                    maxArea = max(maxArea, area)
        return maxArea

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxx = 0
        ROW, COL = len(grid), len(grid[0])
        DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(i, j):
            nonlocal area
            if i < 0 or i == ROW or j < 0 or j == COL or grid[i][j] == 0:
                return 0
            area += 1
            grid[i][j] = 0
            for dr, dc in DIRECTIONS:
                new_i, new_j = i + dr, j + dc
                dfs(new_i, new_j)

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    area = 0
                    dfs(i, j)
                    maxx = max(maxx, area)
        return maxx