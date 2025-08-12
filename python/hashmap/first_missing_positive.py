"""
41. First Missing Positive
https://leetcode.com/problems/first-missing-positive/description/?envType=company&envId=facebook&favoriteSlug=facebook-all
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.



Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.


Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
"""
from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # set all non-positive number to 0
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = 0

        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if 0 <= idx < len(nums) and nums[abs(nums[i]) - 1] != 0:
                nums[idx] = -abs(nums[idx])
            elif 0 <= idx < len(nums) and nums[idx] == 0:
                nums[idx] = -(len(nums) + 1)

        for i in range(len(nums)):
            if nums[i] >= 0:
                return i + 1
        return len(nums) + 1

    # Time Complexity O(nlogn), space O(1)
    def firstMissingPositive(self, nums: List[int]) -> int:
        # [3,4,-1,1]
        #
        # min = 2
        # {3, 4, -1, 1}
        nums.sort()
        k = 1
        for n in nums:
            if n <= 0: continue
            #  1, 2, 2, 3
            #        i
            # k = 3
            if n > k:
                return k
            else:
                k = n + 1

        return k

    # Time Complexity O(n), space O(n)
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 0 1 2 3  4
        # 7,8,9,11,12
        cache_set = set(nums)
        for i in range(len(nums)):
            if i + 1 in cache_set:
                continue
            else:
                return i + 1
        return len(nums) + 1

    def firstMissingPositive(self, nums: List[int]) -> int:
        # 0 1 2 3  4
        # 7,8,9,11,12
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(len(nums)):
            val = abs(nums[i])  # change this idx poistion value to negative. if
            # if the nums[idx] is negative, meaning, idx + 1 exists
            if 1 <= val <= len(nums):
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 * (len(nums) + 1)
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i + 1
        return len(nums) + 1