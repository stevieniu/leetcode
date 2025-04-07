"""
4. https://leetcode.com/problems/median-of-two-sorted-arrays/description/

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).



Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106

"""

from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        total_half = (len(nums1) + len(nums2) + 1) // 2
        half_1 = (len(nums1) + 1) // 2
        l, r = 0, len(nums1)

        # to find :left_max_1 <= right_min_2 and left_max_2 <= right_min_1
        while l <= r:
            partition1 = (l + r) // 2
            partition2 = total_half - partition1

            left_max_1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            right_min_1 = float('inf') if partition1 == len(nums1) else nums1[partition1]

            left_max_2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            right_min_2 = float('inf') if partition2 == len(nums2) else nums2[partition2]

            if left_max_1 <= right_min_2 and left_max_2 <= right_min_1:
                return max(left_max_1, left_max_2) if (len(nums1) + len(nums2)) % 2 != 0 \
                    else (max(left_max_1, left_max_2) + min(right_min_1, right_min_2)) / 2
            elif left_max_1 > right_min_2:
                r = partition1 - 1
            elif left_max_2 > right_min_1:
                l = partition1 + 1
        return -1