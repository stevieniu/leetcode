"""
1762. Buildings With an Ocean View
https://leetcode.com/problems/buildings-with-an-ocean-view/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

There are n buildings in a line. You are given an integer array heights of size n that represents the heights of the buildings in the line.

The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions. Formally, a building has an ocean view if all the buildings to its right have a smaller height.

Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.



Example 1:

Input: heights = [4,2,3,1]
Output: [0,2,3]
Explanation: Building 1 (0-indexed) does not have an ocean view because building 2 is taller.
Example 2:

Input: heights = [4,3,2,1]
Output: [0,1,2,3]
Explanation: All the buildings have an ocean view.
Example 3:

Input: heights = [1,3,2,4]
Output: [3]
Explanation: Only building 3 has an ocean view.


Constraints:

1 <= heights.length <= 105
1 <= heights[i] <= 109
"""
import collections
from typing import List
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        q = collections.deque([])
        max_so_far = 0
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > max_so_far:
                max_so_far = heights[i]
                q.appendleft(i)
        return list(q)

    # monotonic_stack stack
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []  # monotonic decreasing stack, store idx
        for i, h in enumerate(heights):
            while stack and h >= heights[stack[-1]]:
                stack.pop()
            stack.append(i)
        return stack