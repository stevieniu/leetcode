"""
2638. https://leetcode.com/problems/count-the-number-of-k-free-subsets/description/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency

You are given an integer array nums, which contains distinct elements and an integer k.

A subset is called a k-Free subset if it contains no two elements with an absolute difference equal to k. Notice that the empty set is a k-Free subset.

Return the number of k-Free subsets of nums.

A subset of an array is a selection of elements (possibly none) of the array.



Example 1:

Input: nums = [5,4,6], k = 1
Output: 5
Explanation: There are 5 valid subsets: {}, {5}, {4}, {6} and {4, 6}.
Example 2:

Input: nums = [2,3,5,8], k = 5
Output: 12
Explanation: There are 12 valid subsets: {}, {2}, {3}, {5}, {8}, {2, 3}, {2, 3, 5}, {2, 5}, {2, 5, 8}, {2, 8}, {3, 5} and {5, 8}.
Example 3:

Input: nums = [10,5,9,11], k = 20
Output: 16
Explanation: All subsets are valid. Since the total count of subsets is 24 = 16, so the answer is 16.


Constraints:

1 <= nums.length <= 50
1 <= nums[i] <= 1000
1 <= k <= 1000

"""

import collections
from typing import List
class Solution:
    def countTheNumOfKFreeSubsets(self, nums: List[int], k: int) -> int:
        # 2 3 5 8 k = 5
        #     2 ^ 4 - 1 = 16 - 1 = 15
        # (3, 8)
        nums.sort()
        g = collections.defaultdict(list)
        # grouping nums, group numbers whoese num % k the same together
        # e.g. nums = [1, 2, 3, 4, 5, 6], k = 3
        # g= [1, 4],[2, 5], [3, 6].
        # numbers from different groups, their abs must not be k
        # each group is indepenent from others, the total number of combination is cnt1 * cnt2 * ...cntk
        for i, num in enumerate(nums):
            g[num % k].append(num)
        ans = 1
        for arr in g.values():
            # in each arr, the abs of two adajacnet numbers == k
            # so, the combination in arr would be, cannot choose adjacent numbers
            dp = [0] * (len(arr) + 1)  # dp[i] : the count of number of k-fres subsets of arr[:i + 1]
            dp[0] = 1  # empty array
            dp[1] = 2  # only 1 number
            for i in range(2, len(arr) + 1):
                if arr[i - 1] == arr[i - 2] + k:
                    # if chosse arr[i -1], dp[i] = dp[i - 1]
                    # if choose arr[i -2], dp[i] = dp[i - 2]
                    dp[i] = dp[i - 1] + dp[i - 2]
                else:
                    dp[i] = dp[i - 1] * 2
            ans *= dp[-1]
        return ans


