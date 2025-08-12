"""
169. Majority Element
https://leetcode.com/problems/majority-element/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2


Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109


Follow-up: Could you solve the problem in linear time and in O(1) space?

"""
from typing import List
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return max(counter, key=counter.get)

    # Boyer-Moore Voting Algorithm:
    # Because this majority element occurs more than n/2 (floor value) times, even if other elements will 'vote against it', it will win
    def majorityElement(self, nums: List[int]) -> int:
        # 2,2,1,1,1,2,2
        #              i
        # cnt = 3
        ans = cnt = 0
        for n in nums:
            if cnt == 0:
                ans = n
            cnt += 1 if ans == n else -1
        return ans