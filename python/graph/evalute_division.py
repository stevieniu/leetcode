"""
399. Evaluate Division
https://leetcode.com/problems/evaluate-division/description/

You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.



Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation:
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0
Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]
Example 3:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]


Constraints:

1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj consist of lower case English letters and digits.
"""
from typing import List
import collections

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        mapping = collections.defaultdict(dict)
        for (x, y), val in zip(equations, values):
            mapping[x][y] = val
            mapping[y][x] = 1 / val

        # x / y
        def dfs(x, y, visit):
            if x not in mapping or y not in mapping:
                return -1
            if y in mapping[x]:
                return mapping[x][y]

            for i in mapping[x]:
                if i in visit: continue
                visit.add(i)
                tmp = dfs(i, y, visit)
                if tmp == -1: continue
                return mapping[x][i] * tmp
            return -1

        ans = []
        for x, y in queries:
            ans.append(dfs(x, y, set()))
        return ans

    # union find
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = {}  # x: (y, value), value = x / y,  y is the root of x

        # a / b = 2 => {a: (b, 2), b: (b, 1)}
        def find(x):  # return root of x, weight from x to root of x
            if x not in g:
                g[x] = (x, 1)
            group_id, weight = g[x]
            if group_id != x:
                new_group_id, group_weight = find(group_id)
                g[x] = (new_group_id, group_weight * weight)
            return g[x]

        def union(x, y, value):  # x
            group_id_x, weight_x = find(x)
            group_id_y, weight_y = find(y)
            if group_id_x == group_id_y:
                return False
            g[group_id_x] = (group_id_y, weight_y * value / weight_x)
            return True

        for (u, v), value in zip(equations, values):
            union(u, v, value)

        ans = []
        for x, y in queries:
            if x not in g or y not in g:
                ans.append(-1)
            else:
                g_1, w_1 = find(x)
                g_2, w_2 = find(y)
                if g_1 != g_2:
                    ans.append(-1)
                else:
                    ans.append(w_1 / w_2)
        return ans
equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a", "a"]]
print(Solution().calcEquation(equations, values, queries))