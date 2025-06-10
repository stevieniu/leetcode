"""
31. Next Permutation
https://leetcode.com/problems/next-permutation/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.



Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]


Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100
"""
from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        # starting from right, looking for the pivot idx, where nums[i] > nums[i - 1], i is the pivot idx
        pivot_idx = 0
        for i in range(N - 1, 0, -1):
            if nums[i] > nums[i - 1]: # 1, 2, 4, 3 | 4, 3
                pivot_idx = i
                break
        if pivot_idx == 0: # nums is in decending order, just sort it in accesending order
            nums.sort()
            return
        # swap pivot_idx - 1 with first idx bigger than nums[pivot_idx - 1], starting from pivot_idx
        for i in range(N - 1, pivot_idx - 1, -1):
            if nums[i] > nums[pivot_idx - 1]:
                nums[i], nums[pivot_idx - 1] = nums[pivot_idx - 1], nums[i]
                break
        # sort num starting from pivoit_id to end
        nums[pivot_idx:] = sorted(nums[pivot_idx:])