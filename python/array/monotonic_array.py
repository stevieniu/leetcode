"""
896. Monotonic Array
https://leetcode.com/problems/monotonic-array/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.



Example 1:

Input: nums = [1,2,2,3]
Output: true
Example 2:

Input: nums = [6,5,4,4]
Output: true
Example 3:

Input: nums = [1,3,2]
Output: false


Constraints:

1 <= nums.length <= 105
-105 <= nums[i] <= 105
"""


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)

        store = 0
        for i in range(n - 1):
            if nums[i + 1] > nums[i]:
                if store == -1:
                    return False
                else:
                    store = 1
            elif nums[i + 1] < nums[i]:
                if store == 1:
                    return False
                else:
                    store = -1
        return True
