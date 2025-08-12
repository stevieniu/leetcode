"""
198. House Robber
https://leetcode.com/problems/house-robber/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.



Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.


Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400
"""
from typing import List
from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        # i, index in nums; dfs(i) -> max amount at index i
        @lru_cache(None)
        def dfs(i):
            if i >= len(nums):  # out of bounds, no more money can rob
                return 0
            # if rob this house, can't rob next one,
            # if not rob this house, can rob next one
            return max(nums[i] + dfs(i + 2), dfs(i + 1))

        return dfs(0)

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)  # dp[i] max amount at index i
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        return dp[-1]