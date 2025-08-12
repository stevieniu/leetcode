"""
540. Single Element in a Sorted Array
https://leetcode.com/problems/single-element-in-a-sorted-array/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.



Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10


Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 105
"""
from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # 0 1 2 3 4  5 6
        # l
        # 3,3,7,7,10,10,11
        #                r
        #       m
        # l = 0, r = 6, m = 3, a[3], lb =2, move right
        # l = 4, r = 6, m = 5, a[5] = 10, lb =4 , move right
        # l = 6, r = 6, m = 6, a[6] = 11 ,lb = 6, move left
        # l= 6, r = 5 ,return l

        # 0 1 2 3 4 5 6 7 8
        # 1,1,2,3,3,4,4,8,8
        #
        # l = 0, r = 8. m = 4, a[m] = 5. lb = 5, odd, move left
        # l = 0, r = 3, m = 1, a[1] = 1, lb = 0, even, move right
        # l = 2, r = 3, m = 2, a[2] = 2, return 2
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2
            # looking for left boundary. left boundary: the left index whose value == right index value. if the left boundary index is even, means. on the left part, there is no single element,
            # move right. if left boundary index is odd, means, the left part is single elment, move left
            if m == 0:
                if nums[m] == nums[m + 1]:  # m is the left bounary, which is 0, move right
                    l = m + 1
                else:
                    return nums[m]
            elif m == len(nums) - 1:
                if nums[m] == nums[m - 1]:
                    r = m - 1
                else:
                    return nums[m]
            elif nums[m] != nums[m + 1] and nums[m] != nums[m - 1]:
                return nums[m]
            else:
                if nums[m] == nums[m - 1]:
                    if m % 2 == 1:  # left boundary is even, move right
                        l = m + 1
                    else:
                        r = m - 1
                elif nums[m] == nums[m + 1]:
                    if m % 2 == 1:
                        r = m - 1
                    else:
                        l = m + 1




