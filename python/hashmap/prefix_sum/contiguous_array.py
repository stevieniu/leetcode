"""
525. Contiguous Array
https://leetcode.com/problems/contiguous-array/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.



Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Example 3:

Input: nums = [0,1,1,1,1,1,0,0,0]
Output: 6
Explanation: [1,1,1,0,0,0] is the longest contiguous subarray with equal number of 0 and 1.


Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # 0 1 2 3 4 5 6 7 8
        # 0,1,1,1,1,1,0,0,0
        #                 i
        # {-1: 0, 0: 1, 1: 2, 2: 3, 3: 4, 4: 5}
        # 1
        # max = 4 8 - 2 = 6
        #
        # 0 1 0 1
        #       i
        #{-1 : 0, 0: 1}
        # max = 2
        balance = 0 # balance: the number of extra 1. balance == 0 => count[1] == count[0]; balance > 0 => count[1] > count[0]; balance < 0 => count[1] < count[0]
        diff_index = {} # count of ones - count of zeros: ending index
        ans = 0
        for i, n in enumerate(nums):
            balance += 1 if nums[i] == 1 else -1
            if balance not in diff_index:
                diff_index[balance] = i
            if balance == 0:
                ans = i  +  1
            else:
                ans = max(ans, i - diff_index[balance])
        return ans
