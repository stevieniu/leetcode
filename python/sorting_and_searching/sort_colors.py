"""
75. Sort Colors
https://leetcode.com/problems/sort-colors/description/

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.



Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]


Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.


Follow up: Could you come up with a one-pass algorithm using only constant extra space?
"""

from typing import List
class Solution:
    # two pointers
    # def sortColors(self, nums: List[int]) -> None:
    #     n = len(nums)
    #     l, r = 0, n - 1
    #     i = 0
    #     while i <= r :
    #         if nums[i] == 2:
    #             nums[i], nums[r] = nums[r], nums[i]
    #             r -= 1
    #         elif nums[i] == 0:
    #             nums[i], nums[l] = nums[l], nums[i]
    #             i += 1
    #             l += 1
    #         else:
    #             i += 1

    # counting sort
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        counts = [0] * 3

        for x in nums:
            counts[x] += 1

        i = 0
        for c in range(3):
            while counts[c] > 0:
                nums[i] = c
                i += 1
                counts[c] -= 1
















