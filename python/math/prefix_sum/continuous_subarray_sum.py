"""
523. Continuous Subarray Sum
https://leetcode.com/problems/continuous-subarray-sum/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

its length is at least two, and
the sum of the elements of the subarray is a multiple of k.
Note that:

A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.


Example 1:

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
Example 2:

Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
Example 3:

Input: nums = [23,2,6,4,7], k = 13
Output: false


Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
0 <= sum(nums[i]) <= 231 - 1
1 <= k <= 231 - 1
"""
from typing import List
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # 23,2,4,6,7
        # l
        # 25 % 6 = 1
        # {23 % 6: 0, (23 + 2) % 6 : 1, } (23 + 2 + 4) % 6 == 23 % 6.
        #  means the new addition of sum is k multiple. ending idx is 3. 3 - 0 + 1 = 3
        mapping = {0: -1} # total sum up to current index : current index
        # intial 0: -1 because if the sum if starting from begining up to current index, the sum is muliple of k, the current index is the ans, to initialize 0: -1 is easy to code
        total = 0
        for i, num in enumerate(nums):
            total += num
            remainder = total % k
            if remainder not in mapping:
                mapping[remainder] = i
            elif i - mapping[remainder] > 1:
                return True
        return False
        # [23,2,4,6,6]
        #         i
        # {23 % 7 (2): 0, 25 % 7 (4): 1, 29 % 7(1): 2, 35 % 7(0): 3}