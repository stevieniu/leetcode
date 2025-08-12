"""
78. Subsets
https://leetcode.com/problems/subsets/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]


Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""

from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []

        def dsf(i=0):
            if i == len(nums):
                res.append(sol.copy())
                return

            sol.append(nums[i])
            dsf(i + 1)

            sol.pop()
            dsf(i + 1)

        dsf()
        return res

    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(i, combo):
            ans.append(combo.copy())
            for j in range(i, len(nums)):
                combo.append(nums[j])
                dfs(j + 1, combo)
                combo.pop()

        ans = []
        dfs(0, [])
        return ans
nums = [1,2,3]

Solution().subsets(nums)