"""
419. Battleships in a Board
https://leetcode.com/problems/battleships-in-a-board/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.

Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).



Example 1:


Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
Output: 2
Example 2:

Input: board = [["."]]
Output: 0


Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is either '.' or 'X'.


Follow up: Could you do it in one-pass, using only O(1) extra memory and without modifying the values board?
"""

from typing import List
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ROW, COL = len(board), len(board[0])
        cnt = 0
        visit = set()

        def dfs(i, j):
            nonlocal cnt
            if i < 0 or i == ROW or j < 0 or j == COL or (i, j) in visit or board[i][j] != 'X':
                return

            visit.add((i, j))
            for dr, dc in DIRECTIONS:
                new_i, new_j = i + dr, j + dc
                dfs(new_i, new_j)

        for i in range(ROW):
            for j in range(COL):
                if board[i][j] == 'X' and (i, j) not in visit:
                    cnt += 1
                    dfs(i, j)
        return cnt

    def countBattleships(self, board: List[List[str]]) -> int:
        ROW, COL = len(board), len(board[0])
        cnt = 0
        for i in range(ROW):
            for j in range(COL):
                if board[i][j] == 'X':
                    # check if (i, j) is in the middle battleships
                    if j > 0 and board[i][j - 1] == 'X':
                        continue
                    elif i > 0 and board[i - 1][j] == 'X':
                        continue
                    else:
                        cnt += 1
        return cnt


