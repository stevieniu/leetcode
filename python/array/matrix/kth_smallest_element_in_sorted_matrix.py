"""
378. Kth Smallest Element in a Sorted Matrix
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2).



Example 1:

Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
Example 2:

Input: matrix = [[-5]], k = 1
Output: -5


Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 300
-109 <= matrix[i][j] <= 109
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n2


Follow up:

Could you solve the problem with a constant memory (i.e., O(1) memory complexity)?
Could you solve the problem in O(n) time complexity? The solution may be too advanced for an interview but you may find reading this paper fun.
"""

from typing import List
class Solution:

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        N = len(matrix)

        def less_count(target):  # count how many elements smaller than or equal to target
            i, j = N - 1, 0  # starting from last row, first col, due to sorted matrix properties
            cnt = 0
            while i >= 0 and j < N:
                if matrix[i][j] <= target:
                    j += 1
                    cnt += i + 1
                else:
                    i -= 1
            return cnt
            # for r in range(N):
            #     cnt = bisect_right(matrix[r], target)
            #     res += cnt
            # return res

        l, r = matrix[0][0], matrix[N - 1][N - 1]
        while l < r:
            m = l + (r - l) // 2
            if less_count(m) < k:
                l = m + 1
            else:
                r = m
        return l

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def find_uppper_bound(nums, target):  # l, r index
            m = -1
            l, r = 0, len(nums) - 1
            while l <= r:
                m = l + (r - l) // 2
                if nums[m] <= target:
                    l = m + 1
                else:
                    r = m - 1
            return l

        lo, hi = matrix[0][0], matrix[-1][-1]
        N = len(matrix)
        while lo < hi:
            m = lo + (hi - lo) // 2
            cnt = 0
            for i in range(N):
                cnt += find_uppper_bound(matrix[i], m)
            if cnt < k:
                lo = m + 1
            else:
                hi = m
        return lo
