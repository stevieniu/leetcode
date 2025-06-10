"""
827. Making A Large Island
https://leetcode.com/problems/making-a-large-island/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.



Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:

Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:

Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.


Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 500
grid[i][j] is either 0 or 1.
"""
from typing import List
from collections import defaultdict

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        DIRECTIONS = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        N = len(grid)
        areas = defaultdict(int)

        def dfs(r, c, label):
            if r < 0 or r == N or c < 0 or c == N or grid[r][c] != 1:
                return 0

            grid[r][c] = label
            size = 1
            for dr, dc in DIRECTIONS:
                i, j = r + dr, c + dc
                size += dfs(i, j, label)
            return size

        label = 2
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    areas[label] = dfs(r, c, label)
                    label += 1

        def connect(r, c):
            visit = set()
            res = 1
            for dr, dc in DIRECTIONS:
                i, j = r + dr, c + dc
                if 0 <= i < N and 0 <= j < N and grid[i][j] not in visit:
                    res += areas[grid[i][j]]
                    visit.add(grid[i][j])
            return res

        res = 0 if not areas else max(
            areas.values())  # inilizie this because there will be a case like 1,1,1, the while grid is an island, in this case, below code won't be executed
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 0:
                    res = max(res, connect(r, c))
        return res
