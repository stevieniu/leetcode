"""
85. Maximal Rectangle
https://leetcode.com/problems/maximal-rectangle/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.



Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
Example 2:

Input: matrix = [["0"]]
Output: 0
Example 3:

Input: matrix = [["1"]]
Output: 1


Constraints:

rows == matrix.length
cols == matrix[i].length
1 <= row, cols <= 200
matrix[i][j] is '0' or '1'.
"""

from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        max_area = 0
        for i in range(len(matrix)):
            histogram = []
            for j in range(len(matrix[0])):
                k = i
                height = 0
                while k >= 0 and int(matrix[k][j]):
                    height += int(matrix[k][j])
                    k -= 1
                histogram.append(int(height))
            max_area = max(max_area, self.maximal_area(histogram))
        return max_area

    def maximal_area(self, histogram: List[int]) -> int:
        stack = []  # (idx, height)
        max_area = 0
        n = len(histogram)
        for i, height in enumerate(histogram):
            start = i
            while len(stack) > 0 and height < stack[-1][1]:
                idx, h = stack.pop()
                start = idx
                max_area = max(max_area, (i - start) * h)
            stack.append((start, height))

        for i in range(len(stack)):
            max_area = max(max_area, (n - stack[i][0]) * stack[i][1])
        return max_area


    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        ROW, COL = len(matrix), len(matrix[0])
        histograms = [[0] * COL for _ in range(
            ROW)]  # ROW x COL, every row is a histogram, there are ROW histograms in the histograms matrix

        def build_histogram():
            for j in range(COL):
                histograms[0][j] = 1 if matrix[0][j] == '1' else 0
            for i in range(1, ROW):
                for j in range(COL):
                    histograms[i][j] = 0 if matrix[i][j] == '0' else histograms[i - 1][j] + 1

        def calc_max_histogram_area(histogram):
            max_area = 0
            stack = []  # (h, i)
            for i, height in enumerate(histogram):
                start = i
                while stack and height < stack[-1][0]:
                    h, j = stack.pop()
                    width = i - j
                    max_area = max(max_area, width * h)
                    start = j
                stack.append((height, start))
            while stack:
                h, j = stack.pop()
                width = len(histogram) - j
                max_area = max(max_area, width * h)
            return max_area

        build_histogram()
        max_area = 0
        for i in range(ROW):
            max_area = max(max_area, calc_max_histogram_area(histograms[i]))
        return max_area