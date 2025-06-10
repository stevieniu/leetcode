"""
360. Sort Transformed Array
https://leetcode.com/problems/sort-transformed-array/description/?envType=company&envId=linkedin&favoriteSlug=linkedin-three-months

Given a sorted integer array nums and three integers a, b and c, apply a quadratic function of the form f(x) = ax2 + bx + c to each element nums[i] in the array, and return the array in a sorted order.



Example 1:

Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
Output: [3,9,15,33]
Example 2:

Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
Output: [-23,-5,1,7]


Constraints:

1 <= nums.length <= 200
-100 <= nums[i], a, b, c <= 100
nums is sorted in ascending order.


Follow up: Could you solve it in O(n) time?
"""

from sortedcontainers import SortedList
from typing import List
class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        arr = SortedList()
        for num in nums:
            val = a * num * num + b * num + c
            arr.add(val)
        return list(arr)


    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def get_number(x):
            return a * x * x + b * x + c

        l, r = 0, len(nums) - 1
        idx = len(nums) - 1 if a > 0 else 0
        ans = [float('inf')] * len(nums)
        while l <= r:
            left_num = get_number(nums[l])
            right_num = get_number(nums[r])
            if a > 0:
                if left_num < right_num:
                    ans[idx] = right_num
                    r -= 1
                else:
                    ans[idx] = left_num
                    l += 1
                idx -= 1
            else:
                if left_num < right_num:
                    ans[idx] = left_num
                    l += 1
                else:
                    ans[idx] = right_num
                    r -= 1
                idx += 1

        return ans