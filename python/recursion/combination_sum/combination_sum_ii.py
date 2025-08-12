"""
40. Combination Sum II
https://leetcode.com/problems/combination-sum-ii/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.



Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]


Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""

from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sol = []
        candidates.sort()

        def backtrack(start, remain):
            if remain == 0:
                res.append(sol.copy())
                return
            if remain < 0:
                return

            prev = -1
            for i in range(start, len(candidates)):
                if prev == candidates[i]:
                    continue
                sol.append(candidates[i])
                backtrack(i + 1, remain - candidates[i])
                sol.pop()
                prev = candidates[i]

        backtrack(0, target)
        return res

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def dfs(i, target, combo):
            if target < 0:
                return
            if target == 0:
                ans.append(combo.copy())
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]: continue
                combo.append(candidates[j])
                dfs(j + 1, target - candidates[j], combo)
                combo.pop()

        ans = []
        dfs(0, target, [])
        return ans
