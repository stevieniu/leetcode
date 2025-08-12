"""
689. Maximum Sum of 3 Non-Overlapping Subarrays
https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

Given an integer array nums and an integer k, find three non-overlapping subarrays of length k with maximum sum and return them.

Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.



Example 1:

Input: nums = [1,2,1,2,6,7,5,1], k = 2
Output: [0,3,5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
Example 2:

Input: nums = [1,2,1,2,1,2,1,2,1], k = 2
Output: [0,2,4]


Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i] < 216
1 <= k <= floor(nums.length / 3)
"""

from typing import List
from functools import lru_cache
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # pre process
        k_sum = [sum(nums[:k])]
        # 1,2,1,2,6,7,5,1
        #   3
        for i in range(k, len(nums)):
            k_sum.append(k_sum[-1] + nums[i] - nums[i - k])

        @lru_cache(None)
        def get_max_sum(i, cnt):  # i is the starting index of the subarray
            if i > len(nums) - k or cnt == 3:
                return 0
            include = k_sum[i] + get_max_sum(i + k, cnt + 1)
            skip = get_max_sum(i + 1, cnt)
            return max(include, skip)

        i = 0
        indices = []
        while i <= len(nums) - k and len(indices) < 3:
            include = k_sum[i] + get_max_sum(i + k, len(indices) + 1)
            skip = get_max_sum(i + 1, len(indices))
            if include >= skip:
                indices.append(i)
                i += k
            else:
                i += 1
        return indices

        #
        # 7,13,20,19,19,2,10,1,1,19
        #

