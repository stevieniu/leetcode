"""
1060. Missing Element in Sorted Array

Given an integer array nums which is sorted in ascending order and all of its elements are unique and given also an integer k, return the kth missing number starting from the leftmost number of the array.



Example 1:

Input: nums = [4,7,9,10], k = 1
Output: 5
Explanation: The first missing number is 5.
Example 2:

Input: nums = [4,7,9,10], k = 3
Output: 8
Explanation: The missing numbers are [5,6,8,...], hence the third missing number is 8.
Example 3:

Input: nums = [1,2,4], k = 3
Output: 6
Explanation: The missing numbers are [3,5,6,7,...], hence the third missing number is 6.


Constraints:

1 <= nums.length <= 5 * 104
1 <= nums[i] <= 107
nums is sorted in ascending order, and all the elements are unique.
1 <= k <= 108


Follow up: Can you find a logarithmic time complexity (i.e., O(log(n))) solution?
"""
from typing import List
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        # 1,2,4 | k = 3
        #      i
        # k = 6
        k += nums[0] - 1
        for n in nums:
            if k >= n:
                k += 1
            else:
                break
        return k

    def missingElement(self, nums: List[int], k: int) -> int:
        k += nums[0] - 1
        #       4,    7,  9,10
        #  1 2 3 4 5 6 7 8 9 10
        #        3     5   6 6
        # number of missing number is nums[i] - (i + 1)
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] - (m + 1) < k:
                l = m + 1
            else:
                r = m - 1
        # l = r + 1
        # arr[r] + more = arr[r] + k - missing number at r = arr[r] + k - (arr[r] - (r + 1))
        # = arr[k] + k - arr[k] + r + 1 = k + r + 1 = k + l
        return k + l