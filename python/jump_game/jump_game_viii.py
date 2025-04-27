"""
2297. https://leetcode.com/problems/jump-game-viii/description/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency

You are given a 0-indexed integer array nums of length n. You are initially standing at index 0. You can jump from index i to index j where i < j if:

nums[i] <= nums[j] and nums[k] < nums[i] for all indexes k in the range i < k < j, or
nums[i] > nums[j] and nums[k] >= nums[i] for all indexes k in the range i < k < j.
You are also given an integer array costs of length n where costs[i] denotes the cost of jumping to index i.

Return the minimum cost to jump to the index n - 1.



Example 1:

Input: nums = [3,2,4,4,1], costs = [3,7,6,4,2]
Output: 8
Explanation: You start at index 0.
- Jump to index 2 with a cost of costs[2] = 6.
- Jump to index 4 with a cost of costs[4] = 2.
The total cost is 8. It can be proven that 8 is the minimum cost needed.
Two other possible paths are from index 0 -> 1 -> 4 and index 0 -> 2 -> 3 -> 4.
These have a total cost of 9 and 12, respectively.
Example 2:

Input: nums = [0,1,2], costs = [1,1,1]
Output: 2
Explanation: Start at index 0.
- Jump to index 1 with a cost of costs[1] = 1.
- Jump to index 2 with a cost of costs[2] = 1.
The total cost is 2. Note that you cannot jump directly from index 0 to index 2 because nums[0] <= nums[1].


Constraints:

n == nums.length == costs.length
1 <= n <= 105
0 <= nums[i], costs[i] <= 105

"""

from typing import List
class Solution:
    def minCost(self, nums: List[int], costs: List[int]) -> int:
        stack_inc, stack_dec = [], []  # store indices before current index i
        nge, nle = [-1] * len(nums), [-1] * len(nums)
        # use descreasing monotonic stack_queue to look for the first greater element than the current number
        # use increasing monotonic stack_queue to look for the first smaller element than the current number
        for i, num in enumerate(nums):
            while stack_dec and num >= nums[stack_dec[-1]]:
                nge[stack_dec.pop()] = i
            stack_dec.append(i)
            while stack_inc and num < nums[stack_inc[-1]]:
                nle[stack_inc.pop()] = i
            stack_inc.append(i)

        dp = [float('inf')] * len(nums)  # dp[i]: minimum cost to just to index i
        dp[0] = 0

        for i in range(len(nums)):
            # nge[i] != -1 means, current index i can jump to position nge[i]
            # the cost of position nge[i] is dp[i] + cost[nge[i]]
            if nge[i] != -1:
                dp[nge[i]] = min(dp[nge[i]], costs[nge[i]] + dp[i])
            # nle[i] != -1 means, current index i can jump to position nle[i]
            # the cost of position nle[i] is dp[i] + cost[nle[i]]
            if nle[i] != -1:
                dp[nle[i]] = min(dp[nle[i]], costs[nle[i]] + dp[i])
        return dp[-1]