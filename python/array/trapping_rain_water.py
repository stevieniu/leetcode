"""
42. Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.



Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9


Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""

from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_l = [0] * n
        max_r = [0] * n
        for i in range(1, n):
            max_l[i] = max(max_l[i - 1], height[i - 1])

        for i in range(n - 2, -1, -1):
            max_r[i] = max(max_r[i + 1], height[i + 1])
        total = 0
        for i in range(n):
            total += max(0, min(max_l[i], max_r[i]) - height[i])
        return total
