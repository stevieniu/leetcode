"""
2799. Count Complete Subarrays in an Array
https://leetcode.com/problems/count-complete-subarrays-in-an-array/description/

You are given an array nums consisting of positive integers.

We call a subarray of an array complete if the following condition is satisfied:

The number of distinct elements in the subarray is equal to the number of distinct elements in the whole array.
Return the number of complete subarrays.

A subarray is a contiguous non-empty part of an array.



Example 1:

Input: nums = [1,3,1,2,2]
Output: 4
Explanation: The complete subarrays are the following: [1,3,1,2], [1,3,1,2,2], [3,1,2] and [3,1,2,2].
Example 2:

Input: nums = [5,5,5,5]
Output: 10
Explanation: The array consists only of the integer 5, so any subarray is complete. The number of subarrays that we can choose is 10.


Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 2000
"""
from typing import List
import collections

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        #
        #     r
        # 5,5,5,5 # as long as nuns[l : r + 1] is complete subarray, nums[l : r + 2], nums[l:r + 3]... are all complete subarays, the number of complete subarrray starting from l is N - r
        #     l
        # {5:0}
        # 1
        # cnt = 4 + 3 = 7
        ans = 0
        l = 0
        data_cnt = collections.defaultdict(int) # number: cnt
        unique_number = len(set(nums))
        for r, c in enumerate(nums):
            data_cnt[c] += 1
            while len(data_cnt) == unique_number:
                ans += len(nums) - r
                data_cnt[nums[l]] -= 1
                if data_cnt[nums[l]] == 0:
                    del data_cnt[nums[l]]
                l += 1
        return ans