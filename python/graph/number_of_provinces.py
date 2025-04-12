"""
547. Number of Provinces
https://leetcode.com/problems/number-of-provinces/description/

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.



Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:


Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3


Constraints:

1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]

"""
from typing import List
import collections

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visit = set()

        def bfs(city):
            visit.add(city)
            q = collections.deque([city])
            while q:
                node = q.popleft()
                for nei, connected in enumerate(isConnected[node]):
                    if connected and nei not in visit:
                        q.append(nei)
                        visit.add(nei)

        provinces = 0
        for city in range(n):
            if city not in visit:
                bfs(city)
                provinces += 1
        return provinces

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visit = set()
        n = len(isConnected)

        def dfs(city):
            visit.add(city)
            for nei, connected in enumerate(isConnected[city]):
                if connected and nei not in visit:
                    dfs(nei)

        cnt = 0
        for city in range(n):
            if city not in visit:
                dfs(city)
                cnt += 1
        return cnt

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        root = [i for i in
                range(n)]  # at beginning, each node's root is itself; index i is root, root[i] is the root of node i
        rank = [1] * n

        def find(x):  # find the root of x
            # a root would be x = root[x]
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]

        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x == root_y:
                return False  # no need to union

            if rank[root_x] > rank[root_y]:  # merge y to x
                root[root_y] = root_x
                rank[root_x] += rank[root_y]
            else:
                root[root_x] = root_y
                rank[root_y] += rank[root_x]
            return True

        cnt = n
        for city in range(n - 1):
            for nei in range(city + 1, n):
                if isConnected[city][nei] and find(city) != find(nei): # find(city) != find(nei) is to prevent duplicate union
                    union(city, nei)
                    cnt -= 1
        return cnt