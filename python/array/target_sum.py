"""
494. Target Sum
https://leetcode.com/problems/target-sum/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.



Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
Example 2:

Input: nums = [1], target = 1
Output: 1


Constraints:

1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000
"""

from typing import List
from functools import lru_cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def dfs(i, total):
            if i == len(nums):
                return 1 if total == target else 0

            return dfs(i + 1, total + nums[i]) + dfs(i + 1, total - nums[i])

        return dfs(0, 0)

    # brute force
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cnt = 0

        def dfs(i, total):
            nonlocal cnt
            if i == len(nums):
                if total == target:
                    cnt += 1
                return
            dfs(i + 1, total + nums[i])
            dfs(i + 1, total - nums[i])

        dfs(0, 0)
        return cnt

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}  # (i, total): total of ways add up to total

        def dfs(i, total):
            if i == len(nums):
                return 1 if total == target else 0

            if (i, total) in cache:
                return cache[(i, total)]
            cache[(i, total)] = dfs(i + 1, total + nums[i]) + dfs(i + 1, total - nums[i])
            return cache[(i, total)]

        return dfs(0, 0)