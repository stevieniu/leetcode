"""
84. Largest Rectangle in Histogram
https://leetcode.com/problems/largest-rectangle-in-histogram/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.



Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4


Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104
"""
from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # (height, index)
        maxx_area = 0
        n = len(heights)

        for i, height in enumerate(heights):
            # only stack is not empty and current height of bar is lower than the height of the top bar of the stack, then pop the element from stack
            start = i
            while stack and height < stack[-1][0]:
                h, j = stack.pop()
                width = i - j
                maxx_area = max(maxx_area, width * h)
                start = j
            stack.append((height, start))
        # calulate bar area left in the stack
        while stack:
            height, j = stack.pop()
            width = n - j
            maxx_area = max(maxx_area, width * height)
        return maxx_area

