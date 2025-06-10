"""
373. Find K Pairs with Smallest Sums
https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/?envType=company&envId=linkedin&favoriteSlug=linkedin-three-months

You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.



Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]


Constraints:

1 <= nums1.length, nums2.length <= 105
-109 <= nums1[i], nums2[i] <= 109
nums1 and nums2 both are sorted in non-decreasing order.
1 <= k <= 104
k <= nums1.length * nums2.length
"""
import heapq
from typing import List
class Solution:
    # def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    #     """
    #     1,7,11

    #     2,4,6

    #     heap = [(1,2)] => [(1, 4), (2, 7)] # add (1, 2)'s neighbour to the heap
    #                    => [(1, 6), (4, 11)] # pop (1, 4), add its neighbour to the heap
    #     ans = [(1, 2)] => [(1, 2), (1, 4)]
    #     """
    #     n1, n2 = len(nums1), len(nums2)
    #     if n1 == 0 or n2 == 0 or k == 0:
    #         return []

    #     min_heap = [[nums1[0] + nums2[0], 0, 0]] # (nums1[i] + nums2[j], i, j)
    #     visit = set([0, 0])
    #     ans = []
    #     while min_heap and k > 0:
    #         min_sum, i, j = heapq.heappop(min_heap)
    #         ans.append([nums1[i], nums2[j]])
    #         k -= 1
    #         if i + 1 < n1 and (i + 1, j) not in visit:
    #             heapq.heappush(min_heap, [nums1[i + 1] + nums2[j], i + 1, j])
    #             visit.add((i + 1, j))
    #         if j + 1 < n2 and (i, j + 1) not in visit:
    #             heapq.heappush(min_heap, [nums1[i] + nums2[j + 1], i, j + 1])
    #             visit.add((i, j + 1))

    #     return ans

    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n1, n2 = len(nums1), len(nums2)
        ans = []
        if n1 == 0 or n2 == 0 or k == 0:
            return ans

        min_heap = [(nums1[0] + nums2[0], 0, 0)] # (sum, i, j)  i-> nums1 index, j -> nums2 index
        visit = set([0, 0])
        while min_heap and k > 0:
            print(min_heap[0])
            min_sum, i, j = heapq.heappop(min_heap)
            ans.append([nums1[i], nums2[j]])
            k -= 1
            if i + 1 < n1 and (i + 1, j) not in visit:
                heapq.heappush(min_heap, (nums1[i + 1] + nums2[j], i + 1, j))
                visit.add((i + 1, j))
            if j + 1 < n2 and (i, j + 1) not in visit:
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))
                visit.add((i, j + 1))
        return ans
