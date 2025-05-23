"""
487. Max Consecutive Ones II
https://leetcode.com/problems/max-consecutive-ones-ii/description/

Given a binary array nums, return the maximum number of consecutive 1's in the array if you can flip at most one 0.



Example 1:

Input: nums = [1,0,1,1,0]
Output: 4
Explanation:
- If we flip the first zero, nums becomes [1,1,1,1,0] and we have 4 consecutive ones.
- If we flip the second zero, nums becomes [1,0,1,1,1] and we have 3 consecutive ones.
The max number of consecutive ones is 4.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 4
Explanation:
- If we flip the first zero, nums becomes [1,1,1,1,0,1] and we have 4 consecutive ones.
- If we flip the second zero, nums becomes [1,0,1,1,1,1] and we have 4 consecutive ones.
The max number of consecutive ones is 4.


Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.


Follow up: What if the input numbers come in one by one as an infinite stream? In other words, you can't store all numbers coming from the stream as it's too large to hold in memory. Could you solve it efficiently?
"""

from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l, r, n = 0, 0, len(nums)
        zero_cnt = 0
        res = 0
        for r in range(n):
            if nums[r] == 0:
                zero_cnt += 1
            while zero_cnt == 2:
                if nums[l] == 0:
                    zero_cnt -= 1
                l += 1
            res = max(res, r - l + 1)

        return res