"""
2307. https://leetcode.com/problems/check-for-contradictions-in-equations/description/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency

You are given a 2D array of strings equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] means that Ai / Bi = values[i].

Determine if there exists a contradiction in the equations. Return true if there is a contradiction, or false otherwise.

Note:

When checking if two numbers are equal, check that their absolute difference is less than 10-5.
The testcases are generated such that there are no cases targeting precision, i.e. using double is enough to solve the problem.


Example 1:

Input: equations = [["a","b"],["b","c"],["a","c"]], values = [3,0.5,1.5]
Output: false
Explanation:
The given equations are: a / b = 3, b / c = 0.5, a / c = 1.5
There are no contradictions in the equations. One possible assignment to satisfy all equations is:
a = 3, b = 1 and c = 2.
Example 2:

Input: equations = [["le","et"],["le","code"],["code","et"]], values = [2,5,0.5]
Output: true
Explanation:
The given equations are: le / et = 2, le / code = 5, code / et = 0.5
Based on the first two equations, we get code / et = 0.4.
Since the third equation is code / et = 0.5, we get a contradiction.


Constraints:

1 <= equations.length <= 100
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
Ai, Bi consist of lowercase English letters.
equations.length == values.length
0.0 < values[i] <= 10.0
values[i] has a maximum of 2 decimal places.
"""


class Solution:
    def checkContradictions(self, equations: List[List[str]], values: List[float]) -> bool:
        def check_equal(a, b):
            return abs(a - b) < 10 ** (-5)

        # build graph
        graph = collections.defaultdict(set)
        for (a, b), val in zip(equations, values):
            if a == b:
                if check_equal(val, 1):
                    continue
                else:
                    return True
            else:
                graph[a].add((b, val))
                graph[b].add((a, 1 / val))

        vals = {}  # {a: imposed value}

        def dfs(cur):
            for nei, r in graph[cur]:
                if nei in vals:
                    if not check_equal(vals[cur] / vals[nei], r):
                        return True
                else:
                    vals[nei] = vals[cur] / r  # because vals[cur] / vals[nei] == r
                    if dfs(nei):
                        return True
            return False

        for node in graph:
            if node not in vals:
                vals[node] = 1
            if dfs(node):
                return True
        return False
