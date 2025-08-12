"""
1679. Max Number of K-Sum Pairs
https://leetcode.com/problems/max-number-of-k-sum-pairs/description/

You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.



Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.


Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= 109
"""
from typing import List
from collections import defaultdict
class Solution:
    # O(n)
    def maxOperations(self, nums: List[int], k: int) -> int:
        cache = defaultdict(int)
        cnt = 0
        for n in nums:
            if cache[k - n] > 0:
                cnt += 1
                cache[k - n] -= 1
            else:
                cache[n] += 1
        return cnt

    # O(nlogn)
    def maxOperations(self, nums: List[int], k: int) -> int:
        #       l
        # 1, 3, 3, 3, 4
        #        r
        # ans = 0
        # sum = 6
        nums.sort()
        l, r = 0, len(nums) - 1
        ans = 0
        while l < r:
            sum = nums[l] + nums[r]
            if sum < k:
                l += 1
            elif sum > k:
                r -= 1
            else:
                l += 1
                r -= 1
                ans += 1
        return ans
