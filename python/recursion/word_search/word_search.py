"""
79. https://leetcode.com/problems/word-search/description/

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.



Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false


Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.


Follow up: Could you use search pruning to make your solution faster with a larger board?
"""

from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROW, COL = len(board), len(board[0])
        visit = set()

        def dfs(i, r, c):
            # i: index i word, (r,c) index on board. dfs(i, r, c) => starting at pos (r, c), can find word[i:] ?
            if i == len(word):
                return True
            if r < 0 or r == ROW or c < 0 or c == COL or board[r][c] != word[i] or (r, c) in visit:
                return False

            visit.add((r, c))
            for dr, dc in DIRECTIONS:
                nxt_r, nxt_c = r + dr, c + dc
                if dfs(i + 1, nxt_r, nxt_c):
                    return True
            visit.discard((r, c))

            return False

        for i in range(ROW):
            for j in range(COL):
                if dfs(0, i, j):
                    return True
        return False