from typing import List
import  collections
import string
from typing import Optional

from math import sqrt
import random


def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
    N = len(grid)
    if grid[0][0] or grid[N - 1][N - 1]: return -1
    DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
    q = collections.deque([(0, 0)])
    ans = 1
    while q:
        for _ in range(len(q)):
            i, j = q.popleft()
            if i == N - 1 and j == N - 1:
                return ans
            grid[i][j] = 1
            for dr, dc in DIRECTIONS:
                nxt_i, nxt_j = i + dr, j + dc
                if nxt_i < 0 or nxt_i == N or nxt_j or nxt_j == N or grid[nxt_i][nxt_j]: continue
                q.append([nxt_i, nxt_j])
        ans += 1
    return ans

grid = [[0,0,0],[1,1,0],[1,1,0]]
print(shortestPathBinaryMatrix(grid))