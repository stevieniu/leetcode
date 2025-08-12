"""
1099. Two Sum Less Than K
https://leetcode.com/problems/two-sum-less-than-k/description/

Given an array nums of integers and integer k, return the maximum sum such that there exists i < j with nums[i] + nums[j] = sum and sum < k. If no i, j exist satisfying this equation, return -1.



Example 1:

Input: nums = [34,23,1,24,75,33,54,8], k = 60
Output: 58
Explanation: We can use 34 and 24 to sum 58 which is less than 60.
Example 2:

Input: nums = [10,20,30], k = 15
Output: -1
Explanation: In this case it is not possible to get a pair sum less that 15.


Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 1000
1 <= k <= 2000
"""
from typing import List
from  bisect import bisect_left
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_sum = float('-inf')
        l, r = 0, len(nums) - 1
        while l < r:
            cur_sum = nums[l] + nums[r]
            if cur_sum < k:
                max_sum = max(max_sum, cur_sum)
                l += 1
            else:
                r -= 1
        return max_sum if max_sum != float('-inf') else -1

    # binary search
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:

        # 34,23,1,24,75,33,54,8
        # l
        # 1, 8, 23, 24, 33, 34, 54, 75
        #       i
        #                            l
        # i = 0, target = 60 - 1 = 59,
        # l = 0, r = 7, m = 3 a[3] = 24, <  59
        # l = 4, r = 7, m = 5, a[5] = 34 < 59
        # l =6, r = 7, m = 6, a[6] = 54 < 59
        # l = 7. r= 7 , a[7] = 75 > 59
        # l = 7, r = 6, => 6 => sum = 54 + 1 = 55
        # i = 1, target = 60 - 8 = 52
        # l = 0, r = 7, m = 4, a[3] = 24 > 52
        # l = 6, r = 7, m = 6, a[6] = 54 > 52
        # l = 6, r = 5, => 5, 34 + 8 = 42
        # i = 2
        # l =
        max_sum = float('-inf')
        nums.sort()
        for i, n in enumerate(nums):
            target = k - n
            j = bisect_left(nums, target, i + 1) - 1
            if j > i:
                max_sum = max(max_sum, nums[i] + nums[j])
        return max_sum if max_sum != float('-inf') else -1

    def twoSumLessThanK(self, nums: List[int], k: int) -> int:

        # 34,23,1,24,75,33,54,8
        # l
        # 1, 8, 23, 24, 33, 34, 54, 75
        #       i
        #                            l
        # i = 0, target = 60 - 1 = 59,
        # l = 0, r = 7, m = 3 a[3] = 24, <  59
        # l = 4, r = 7, m = 5, a[5] = 34 < 59
        # l =6, r = 7, m = 6, a[6] = 54 < 59
        # l = 7. r= 7 , a[7] = 75 > 59
        # l = 7, r = 6, => 6 => sum = 54 + 1 = 55
        # i = 1, target = 60 - 8 = 52
        # l = 0, r = 7, m = 4, a[3] = 24 > 52
        # l = 6, r = 7, m = 6, a[6] = 54 > 52
        # l = 6, r = 5, => 5, 34 + 8 = 42
        # i = 2
        # l =
        def binary_search(l, r, target):
            while l <= r:
                m = l + (r - l) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return r

        max_sum = float('-inf')
        nums.sort()
        for i, n in enumerate(nums):
            target = k - n
            # j = bisect_left(nums, target, i + 1) - 1
            j = binary_search(i + 1, len(nums) - 1, target)
            if j > i:
                print(j, i, max_sum, nums[i] + nums[j])
                max_sum = max(max_sum, nums[i] + nums[j])
        return max_sum if max_sum != float('-inf') else -1