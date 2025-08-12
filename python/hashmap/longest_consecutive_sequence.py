"""
128. Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        maxx = 0
        for num in num_set:
            # only counts when num -1 not in num_Set, because it means num is the consecutive starting point
            if num - 1 in num_set: continue
            cnt = 0
            while num in num_set:
                cnt += 1
                num += 1
            maxx = max(maxx, cnt)
        return maxx

    def longestConsecutive(self, nums: List[int]) -> int:
        # 100,4,200,1,3,2
        #           i.
        # 2- 1 = 1
        # 4
        if not nums:
            return 0
        ans = float('-inf')
        n_set = set(nums)
        for n in nums:
            if n in n_set:
                cnt = 1
                n_set.remove(n)
                tmp = n - 1
                while tmp in n_set:
                    cnt += 1
                    n_set.remove(tmp)
                    tmp -= 1
                tmp = n + 1
                while tmp in n_set:
                    cnt += 1
                    n_set.remove(tmp)
                    tmp += 1
                ans = max(ans, cnt)
        return ans