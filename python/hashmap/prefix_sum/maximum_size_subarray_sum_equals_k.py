"""
325. Maximum Size Subarray Sum Equals k
https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

Given an integer array nums and an integer k, return the maximum length of a subarray that sums to k. If there is not one, return 0 instead.



Example 1:

Input: nums = [1,-1,5,-2,3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
Example 2:

Input: nums = [-2,-1,2,1], k = 1
Output: 2
Explanation: The subarray [-1, 2] sums to 1 and is the longest.


Constraints:

1 <= nums.length <= 2 * 105
-104 <= nums[i] <= 104
-109 <= k <= 109

"""
from typing import List
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        #  -2,-1,2,1   k = 1
        #          i
        # {0: -1, -2 : 0, -3: 1, -1: 2}  3 - 2 = 1
        # max = 2
        cache = {0: -1} # prefix_sum : ending idx
        max_size = float('-inf')
        cur_sum = 0
        for i, n in enumerate(nums):
            cur_sum += n
            if cur_sum - k in cache:
                max_size = max(max_size, i - cache[cur_sum - k])
            if cur_sum not in cache:
                cache[cur_sum] = i
        return max_size if max_size != float('-inf') else 0