"""
2461. https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency

You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

The length of the subarray is k, and
All the elements of the subarray are distinct.
Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

A subarray is a contiguous non-empty sequence of elements within an array.



Example 1:

Input: nums = [1,5,4,2,9,9,9], k = 3
Output: 15
Explanation: The subarrays of nums with length 3 are:
- [1,5,4] which meets the requirements and has a sum of 10.
- [5,4,2] which meets the requirements and has a sum of 11.
- [4,2,9] which meets the requirements and has a sum of 15.
- [2,9,9] which does not meet the requirements because the element 9 is repeated.
- [9,9,9] which does not meet the requirements because the element 9 is repeated.
We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions
Example 2:

Input: nums = [4,4,4], k = 3
Output: 0
Explanation: The subarrays of nums with length 3 are:
- [4,4,4] which does not meet the requirements because the element 4 is repeated.
We return 0 because no subarrays meet the conditions.


Constraints:

1 <= k <= nums.length <= 105
1 <= nums[i] <= 105
"""
from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        #           l
        # 1,5,4,2,9,9,9    k = 3 {  }, sum =9,  MAX = 15
        #           r

        #   l
        # 4 4 4 {4}
        #   r
        l = 0
        data_set = set()
        sum = 0
        ans = 0
        for r in range(len(nums)):
            while nums[r] in data_set:
                sum -= nums[l]
                data_set.remove(nums[l])
                l += 1
            data_set.add(nums[r])
            sum += nums[r]
            if len(data_set) == k:
                ans = max(ans, sum)
            elif len(data_set) > k:
                sum -= nums[l]
                ans = max(ans, sum)
                data_set.remove(nums[l])
                l += 1

        return ans
