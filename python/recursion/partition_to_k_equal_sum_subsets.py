"""
698. Partition to K Equal Sum Subsets
Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.



Example 1:

Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Example 2:

Input: nums = [1,2,3,4], k = 3
Output: false


Constraints:

1 <= k <= nums.length <= 16
1 <= nums[i] <= 104
The frequency of each element is in the range [1, 4].
"""

from typing import List
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target, remain = divmod(sum(nums), k)
        selected_mask = set()
        def dfs(i, k, subset_sum, cur_mask): # starting from i, can split k subsets, with sumbset sum?
            if k == 0:
                return True
            if subset_sum > target:
                return False
            if cur_mask in selected_mask:
                return False

            if subset_sum == target: # find one subset, start over to find others
                ans = dfs(0, k - 1, 0, cur_mask) # only finish all recursion, the cur_mask is complted , and can be ready to add to selected_mast set, so selected_mask.add(cur_mask) must be placed after recursion
                selected_mask.add(cur_mask)
                return ans

            for j in range(i, len(nums)):
                num = nums[j]
                if cur_mask & (1 << j) == 0:
                    cur_mask |= (1 << j)
                    if dfs(j + 1, k, subset_sum + num, cur_mask):
                        return True
                    cur_mask ^= (1 << j)
            return False
        if remain > 0:
            return False
        return dfs(0, k,0, 0)

nums = [4,3,2,3,5,2,1]
k = 4
Solution().canPartitionKSubsets(nums, k)