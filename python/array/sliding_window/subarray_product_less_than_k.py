"""
713. Subarray Product Less Than K
https://leetcode.com/problems/subarray-product-less-than-k/description/

Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.



Example 1:

Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Example 2:

Input: nums = [1,2,3], k = 0
Output: 0


Constraints:

1 <= nums.length <= 3 * 104
1 <= nums[i] <= 1000
0 <= k <= 106
"""

from typing import List
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # .     r
        # 10,5,2,6 | 100
        #    l
        #
        # product = 100
        # ans = 3
        if k == 0 or k == 1:
            return 0
        ans = 0
        l = 0
        product = 1
        for r in range(len(nums)):
            product *= nums[r]
            while product >= k:
                product //= nums[l]
                l += 1

            if product < k:
                ans += r - l + 1  # whenever introduce one number, the new number introduced (r - l + 1) subarrays, (r -l + 1) is the window size
        return ans