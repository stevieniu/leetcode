"""
47. Permutations II
https://leetcode.com/problems/permutations-ii/description/
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.



Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        count = collections.Counter(nums)
        res = []

        def dsf(sol=[]):
            if len(sol) == len(nums):
                res.append(sol.copy())
                return

            for d in count:
                if count[d] > 0:
                    sol.append(d)
                    count[d] -= 1
                    dsf(sol)
                    count[d] += 1
                    sol.pop()

        dsf()
        return res