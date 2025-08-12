"""
286. Walls and Gates
https://leetcode.com/problems/walls-and-gates/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.



Example 1:


Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
Example 2:

Input: rooms = [[-1]]
Output: [[-1]]


Constraints:

m == rooms.length
n == rooms[i].length
1 <= m, n <= 250
rooms[i][j] is -1, 0, or 231 - 1.
"""


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        q = collections.deque([])

        ROW, COL = len(rooms), len(rooms[0])
        for i in range(ROW):
            for j in range(COL):
                if rooms[i][j] == 0:
                    q.append((i, j))

        DIRECTIONS = [[-1, 0], [0, 1], [0, -1], [1, 0]]
        step = 0
        while q:
            size = len(q)

            for _ in range(size):
                i, j = q.popleft()
                for dx, dy in DIRECTIONS:
                    new_i, new_j = i + dx, j + dy
                    if (new_i < 0 or new_i == ROW or new_j < 0 or new_j == COL or
                            rooms[new_i][new_j] != 2147483647): continue
                    rooms[new_i][new_j] = step + 1
                    q.append((new_i, new_j))
            step += 1