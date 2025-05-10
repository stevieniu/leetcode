"""
34. Find First and Last Position of Element in Sorted Array
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/?envType=company&envId=linkedin&favoriteSlug=linkedin-thirty-days

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109

"""
from  typing import  List
import bisect
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binary_search(nums, target, True)
        right = self.binary_search(nums, target, False)
        return [left, right]

    def binary_search(self, nums, target, direction):  # direction = True, search most left, False, search most right
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        pos = -1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                #   p
                # 8 8 8
                # l m r   r = m - 1 = 0 == l
                pos = m
                if direction:  # search most left
                    r = m - 1
                else:
                    l = m + 1
        return pos

    # def searchRange(self, nums: List[int], target: int) -> List[int]:
    #     if not nums: return [-1, -1]
    #     l = bisect.bisect_left(nums, target)
    #     if l < 0 or l == len(nums) or nums[l] != target:
    #         return [-1, -1]
    #     r = bisect.bisect_right(nums, target)
    #     if nums[r - 1] != target:
    #         return [-1, -1]
    #     return [l, r - 1]


nums = [1, 1, 1, 2,2,2,3, 4]
print(Solution().searchRange(nums, 2))

