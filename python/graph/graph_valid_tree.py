"""
261. Graph Valid Tree
https://leetcode.com/problems/graph-valid-tree/description/

You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.



Example 1:


Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
Example 2:


Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false


Constraints:

1 <= n <= 2000
0 <= edges.length <= 5000
edges[i].length == 2
0 <= ai, bi < n
ai != bi
There are no self-loops or repeated edges.


"""

from typing import List
import collections
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
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
            # par[find(x)] = find(y)

        number = n
        for u, v in edges:
            if find(u) == find(v):
                return False
            else:
                union(u, v)
                number -= 1
        return number == 1

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        g = collections.defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        visit = set()

        def dfs(cur, prev):  # cur: cur city, prev: previous visited city
            # return true if no cycle exist, otherwise return False
            if cur in visit:  # cycle exist
                return False
            visit.add(cur)
            for nei in g[cur]:
                if nei == prev: continue
                if not dfs(nei, cur):
                    return False
            return True

        if not dfs(0, -1):
            return False
        return len(visit) == n
