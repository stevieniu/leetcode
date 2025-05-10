"""
1197. Minimum Knight Moves
https://leetcode.com/problems/minimum-knight-moves/description/?envType=company&envId=linkedin&favoriteSlug=linkedin-thirty-days

In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.


Return the minimum number of steps needed to move the knight to the square [x, y]. It is guaranteed the answer exists.



Example 1:

Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]
Example 2:

Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]


Constraints:

-300 <= x, y <= 300
0 <= |x| + |y| <= 300
"""
import collections
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == 0 and y == 0:
            return 0

        DIRECTIONS = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]
        q = collections.deque([(0, 0)])
        visit = set((0, 0))
        step = 0
        while q:
            step += 1
            for _ in range(len(q)):
                cur_x , cur_y = q.popleft()
                for dr, dc in DIRECTIONS:
                    nxt_x, nxt_y = cur_x + dr , cur_y + dc
                    if nxt_x == x and nxt_y == y:
                        return step
                    if (nxt_x, nxt_y) in visit: continue
                    visit.add((nxt_x, nxt_y))
                    q.append((nxt_x, nxt_y))
        return 0
