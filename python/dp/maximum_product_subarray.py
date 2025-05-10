"""
152. Maximum Product Subarray
http://leetcode.com/problems/maximum-product-subarray/description/

Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.



Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any subarray of nums is guaranteed to fit in a 32-bit integer.
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin = curMax = 1

        for n in nums:
            if n == 0:
                curMin = curMax = 1
                continue

            tmp = n * curMax
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax)
        return res
