from typing import List
import collections
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        root = [i for i in range(n)]
        rank = [1] * n

        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry: return False
            if rank[rx] > rank[ry]:
                root[ry] = rx
                rank[rx] += rank[ry]
            else:
                root[rx] = ry
                rank[ry] += rank[rx]
            return True

        g = collections.defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        cnt = n
        for i in range(n):
            for nei in g[i]:
                print(nei, i)
                if find(nei) == find(i): continue
                union(nei, i)
                cnt -= 1
        print(root)
        return cnt == 1

n = 5
edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Solution().validTree(n, edges)