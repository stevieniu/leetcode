"""
329. Longest Increasing Path in a Matrix
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).



Example 1:


Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:


Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
Example 3:

Input: matrix = [[1]]
Output: 1


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 231 - 1
"""
from typing import List
class Solution:
    # brute force, dfs
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        maxx = 1
        ROW, COL = len(matrix), len(matrix[0])
        DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def dfs(i, j, visit, path):
            nonlocal maxx
            if i < 0 or i == ROW or j < 0 or j == COL or (i, j) in visit:
                return
            if path and matrix[i][j] <= path[-1]:
                return

            path.append(matrix[i][j])
            visit.add(matrix[i][j])
            maxx = max(maxx, len(path))

            for dr, dc in DIRECTIONS:
                new_i, new_j = i + dr, j + dc
                dfs(new_i, new_j, visit, path)
            path.pop()
            visit.remove(matrix[i][j])
        for i in range(ROW):
            for j in range(COL):
                dfs(i, j, set(), [])
        return maxx
