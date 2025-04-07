"""
200. https://leetcode.com/problems/number-of-islands/description/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.


"""
from typing import List
import collections
class Solution:
    # dfs 1
    def numIslands(self, grid: List[List[str]]) -> int:
        DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROW, COL = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i == ROW or j < 0 or j == COL or grid[i][j] == '0':
                return

            grid[i][j] = '0'
            for dr, dc in DIRECTIONS:
                nxt_i, nxt_j = i + dr, j + dc
                dfs(nxt_i, nxt_j)

        cnt = 0
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == '1':
                    cnt += 1
                    dfs(i, j)
        return cnt

    # dfs 2, it is faster than dfs1 , because it check if need to do dfs first
    def numIslands(self, grid: List[List[str]]) -> int:
        DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ROW, COL = len(grid), len(grid[0])

        def dfs(i, j):
            grid[i][j] = '0'
            for dr, dc in DIRECTIONS:
                nxt_i, nxt_j = i + dr, j + dc
                if nxt_i < 0 or nxt_i == ROW or nxt_j < 0 or nxt_j == COL or grid[nxt_i][nxt_j] == '0': continue
                dfs(nxt_i, nxt_j)

        cnt = 0
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == '1':
                    cnt += 1
                    dfs(i, j)
        return cnt

    def numIslands(self, grid: List[List[str]]) -> int:
        DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROW, COL = len(grid), len(grid[0])

        # visit = set()

        def bfs(i, j):
            q = collections.deque([(i, j)])

            while q:
                cur_i, cur_j = q.popleft()
                for dr, dc in DIRECTIONS:
                    nxt_i, nxt_j = cur_i + dr, cur_j + dc
                    if nxt_i < 0 or nxt_i == ROW or nxt_j < 0 or nxt_j == COL or \
                            grid[nxt_i][nxt_j] == '0':
                        continue
                    grid[nxt_i][nxt_j] = '0'
                    q.append((nxt_i, nxt_j))

        ans = 0
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == '1':
                    bfs(i, j)
                    ans += 1
        return ans
