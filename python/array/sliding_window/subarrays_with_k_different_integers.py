"""
992. Subarrays with K Different Integers
https://leetcode.com/problems/subarrays-with-k-different-integers/description/

Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.



Example 1:

Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
Example 2:

Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].


Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i], k <= nums.length
"""
from typing import List
import collections

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        #       f
        #       n
        # 1,2,2,1,3
        #         r
        #
        # {1: 1, 3: 1}
        # cnt= 5
        # sliding window, with 3 ptrs, right pointer r, left near pointer l_near, [l_near, r]=> min size of the window
        # left far pointer l_far [l_far, r] => max size of the window
        # ans += l_near - l_far + 1
        ans = 0
        counter = collections.defaultdict(int)  # number: cnt
        l_far = l_near = 0
        for r in range(len(nums)):
            counter[nums[r]] += 1
            while len(counter) > k:
                counter[nums[l_near]] -= 1
                if counter[nums[l_near]] == 0:
                    del counter[nums[l_near]]
                l_near += 1
                l_far = l_near

            while counter[nums[l_near]] > 1:
                counter[nums[l_near]] -= 1
                l_near += 1
            if len(counter) == k:
                ans += l_near - l_far + 1

        return ans
