"""
209. Minimum Size Subarray Sum
https://leetcode.com/problems/minimum-size-subarray-sum/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.



Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0


Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104


Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
"""
from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #           i
        # 2,3,1,2,4,3.  7
        #.          j
        # sum = 7,   min = 3
        if not nums: return 0
        l, r, n = 0, 0, len(nums)
        min_len = float('inf')
        local_sum = 0

        for r in range(n):
            local_sum += nums[r]
            while local_sum >= target:
                min_len = min(min_len, r - l + 1)
                local_sum -= nums[l]
                l += 1
        return 0 if min_len == float('inf') else min_len

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # prefix_sum = [1, 3, 6, 10, 15]
        #
        # sum[i : j] = prefix_sum[j] - prefix_sum[i - 1] if i - 1 >= 0 else prefix_sum[j]
        # i = 0,
        # l = 0, r = 4, m = 2, s[0:2] = P[2] = 6 < 15,
        # l = 3. r = 4, m = 3. s[0:3] = p[3] = 10 < 15
        # l = 4. r= 4. ,m = 4. s[0:4] = p[4] = 15 == 15 len = 5

        prefix_sum = [0] * len(nums)
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            prefix_sum[i] = cur_sum
        # print(prefix_sum)
        min_len = float('inf')
        for i in range(len(nums)):
            l, r = i, len(nums) - 1
            while l <= r:
                m = l + (r - l) // 2
                partial_sum = prefix_sum[m] - prefix_sum[i - 1] if i - 1 >= 0 else prefix_sum[m]
                if partial_sum < target:
                    l = m + 1
                else:
                    min_len = min(min_len, m - i + 1)
                    r = m - 1
        return min_len if min_len != float('inf') else 0