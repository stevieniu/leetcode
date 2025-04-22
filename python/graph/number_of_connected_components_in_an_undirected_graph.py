"""
323. Number of Connected Components in an Undirected Graph
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/

You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.



Example 1:


Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
Example 2:


Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1


Constraints:

1 <= n <= 2000
1 <= edges.length <= 5000
edges[i].length == 2
0 <= ai <= bi < n
ai != bi
There are no repeated edges.
"""
import collections
from typing import List
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n
        def find(x):
            if x == par[x]:
                return x
            else:
                par[x] = find(par[x])
            return par[x]

        def union(x, y):
            p1, p2 = find(x), find(y)
            if p1 != p2:
                if rank[p1] > rank[p2]:
                    par[p2] = p1
                    rank[p1] += rank[p2]
                else:
                    par[p1] = p2
                    rank[p2] += rank[p1]

        number = n
        for u, v in edges:
            if find(u) != find(v):
                union(u, v)
                number -= 1
        return number

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g = collections.defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        visit = set()

        def dfs(cur, prev):
            visit.add(cur)
            for nei in g[cur]:
                if nei == prev: continue
                if nei not in visit:
                    dfs(nei, cur)

        cnt = 0
        for i in range(n):
            if i not in visit:
                cnt += 1
                dfs(i, -1)
        return cnt