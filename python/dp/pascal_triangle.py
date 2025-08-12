"""
118. Pascal's Triangle
https://leetcode.com/problems/pascals-triangle/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:




Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]


Constraints:

1 <= numRows <= 30
"""
from typing import List
class Solution:
    # def generate(self, numRows: int) -> List[List[int]]:
    #     res = []
    #     for i in range(1, numRows + 1):
    #         row = [0] * i
    #         row[0], row[-1] = 1, 1
    #         for c in range(1, i - 1):
    #             row[c] = res[-1][c - 1] + res[-1][c]
    #         res.append(row)
    #     return res
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for r in range(1, numRows):
            row = [0] * (r + 1)
            for c in range(r + 1):
                if c == 0 or c == r:
                    row[c] = 1
                else:
                    row[c] = res[-1][c - 1] + res[-1][c]
            res.append(row)
        return res

    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(1, numRows + 1):
            if i == 1 or i == 2:
                ans.append([1] * i)
            else:
                lvl = [1] * i
                for j in range(1, i - 1):
                    lvl[j] = ans[-1][j - 1] + ans[-1][j]
                ans.append(lvl)
        return ans