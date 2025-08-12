"""
643. Maximum Average Subarray I
https://leetcode.com/problems/maximum-average-subarray-i/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.



Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000


Constraints:

n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104
"""
from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #       l
        # 1,12,-5,-6,50,3
        #               r
        # 51 / 4
        # prefix_sum = 54 - 12 = 42
        #max = 12.75

        prefix_sum = 0
        for i in range(k):
            prefix_sum += nums[i]
        max_avg = prefix_sum / k
        for i in range(k, len(nums)):
            prefix_sum += nums[i]
            prefix_sum -= nums[i - k]
            max_avg = max(max_avg, prefix_sum / k)
        return max_avg