"""
317. Shortest Distance from All Buildings
https://leetcode.com/problems/shortest-distance-from-all-buildings/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

You are given an m x n grid grid of values 0, 1, or 2, where:

each 0 marks an empty land that you can pass by freely,
each 1 marks a building that you cannot pass through, and
each 2 marks an obstacle that you cannot pass through.
You want to build a house on an empty land that reaches all buildings in the shortest total travel distance. You can only move up, down, left, and right.

Return the shortest travel distance for such a house. If it is not possible to build such a house according to the above rules, return -1.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.



Example 1:


Input: grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
Output: 7
Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2).
The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal.
So return 7.
Example 2:

Input: grid = [[1,0]]
Output: 1
Example 3:

Input: grid = [[1]]
Output: -1


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0, 1, or 2.
There will be at least one building in the grid.
"""
import collections
from typing import List

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ROW, COL = len(grid), len(grid[0])
        EMPTY, BUILDING, BLOCK = 0, 1, 2
        buildings = 0
        dist_matrix = [[0] * COL for _ in range(ROW)]
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == BUILDING:  # BFS starting from each building
                    buildings += 1
                    q = collections.deque([(i, j)])
                    dist = 0
                    while q:
                        dist += 1
                        for _ in range(len(q)):
                            r, c = q.popleft()
                            for dr, dc in DIRECTIONS:
                                new_r, new_c = r + dr, c + dc
                                if new_r < 0 or new_r == ROW or new_c < 0 or new_c == COL or \
                                        grid[new_r][new_c] != EMPTY:
                                    continue
                                dist_matrix[new_r][new_c] += dist
                                grid[new_r][new_c] -= 1
                                q.append((new_r, new_c))
                    EMPTY -= 1
        # print(dist_matrix)
        # print(grid)
        # print(buildings)
        ans = float('inf')
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == -buildings:
                    print(dist_matrix[i][j])
                    ans = min(ans, dist_matrix[i][j])

        return ans if ans != float('inf') else -1

