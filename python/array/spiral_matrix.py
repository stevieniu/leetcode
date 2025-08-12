"""
54. Spiral Matrix
https://leetcode.com/problems/spiral-matrix/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

Given an m x n matrix, return all elements of the matrix in spiral order.



Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROW, COL = len(matrix), len(matrix[0])
        RIGHT, DOWN, LEFT, UP = 0, 1, 2, 3
        UP_WALL, RIGHT_WALL, DOWN_WALL, LEFT_WALL = 0, COL, ROW, -1
        direction = RIGHT
        ans = []
        i, j = 0, 0
        while len(ans) < ROW * COL:
            # RIGHT
            if direction == RIGHT:
                while j < RIGHT_WALL:
                    ans.append(matrix[i][j])
                    j += 1
                i, j = i + 1, j - 1
                RIGHT_WALL -= 1
                direction = DOWN
            # DOWN
            elif direction == DOWN:
                while i < DOWN_WALL:
                    ans.append(matrix[i][j])
                    i += 1
                i, j = i - 1, j - 1
                DOWN_WALL -= 1
                direction = LEFT
            # LEFT
            elif direction == LEFT:
                while j > LEFT_WALL:
                    ans.append(matrix[i][j])
                    j -= 1
                i, j = i - 1, j + 1
                LEFT_WALL += 1
                direction = UP
            # UP
            else:
                while i > UP_WALL:
                    ans.append(matrix[i][j])
                    i -= 1
                i, j = i + 1, j + 1
                UP_WALL += 1
                direction = RIGHT
        return ans