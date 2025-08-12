"""
90. Subsets II
https://leetcode.com/problems/subsets-ii/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]


Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10

"""

from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        sol = []

        def dsf(i=0):
            if i == len(nums):
                res.append(sol.copy())
                return

            sol.append(nums[i])
            dsf(i + 1)

            sol.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dsf(i + 1)

        dsf()
        return res

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def dfs(i, combo):
            ans.append(combo.copy())
            for j in range(i, len(nums)):
                if j != i and nums[j] == nums[j - 1]:
                    continue
                combo.append(nums[j])
                dfs(j + 1, combo)
                combo.pop()

        ans = []
        dfs(0, [])
        return ans

