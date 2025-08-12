"""
498. Diagonal Traverse
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.



Example 1:


Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
Example 2:

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]


Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
-105 <= mat[i][j] <= 105
"""

from typing import List
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        direction = True  # true -> diagnol, false, anti-diagnol
        ROW, COL = len(mat), len(mat[0])
        i, j = 0, 0
        res = [mat[i][j]]
        cnt = ROW * COL - 1
        while cnt > 0:
            if direction:
                new_i, new_j = i - 1, j + 1
                if new_i < 0 or new_i >= ROW or new_j <= 0 or new_j >= COL:
                    if new_j >= COL:
                        new_i, new_j = i + 1, j
                    elif new_i < 0:
                        new_i, new_j = i, j + 1
                    direction = not direction
            else:
                new_i, new_j = i + 1, j - 1
                if new_i < 0 or new_i >= ROW or new_j < 0 or new_j >= COL:
                    if new_i >= ROW:
                        new_i, new_j = i, j + 1
                    elif new_j < 0:
                        new_i, new_j = i + 1, j
                    direction = not direction

            i, j = new_i, new_j
            res.append(mat[i][j])
            cnt -= 1

        return res


