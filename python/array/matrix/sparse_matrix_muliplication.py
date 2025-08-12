"""
311. Sparse Matrix Multiplication
https://leetcode.com/problems/sparse-matrix-multiplication/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

Given two sparse matrices mat1 of size m x k and mat2 of size k x n, return the result of mat1 x mat2. You may assume that multiplication is always possible.



Example 1:


Input: mat1 = [[1,0,0],[-1,0,3]], mat2 = [[7,0,0],[0,0,0],[0,0,1]]
Output: [[7,0,0],[-7,0,3]]
Example 2:

Input: mat1 = [[0]], mat2 = [[0]]
Output: [[0]]


Constraints:

m == mat1.length
k == mat1[i].length == mat2.length
n == mat2[i].length
1 <= m, n, k <= 100
-100 <= mat1[i][j], mat2[i][j] <= 100
"""
from typing import List

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        # A[mxn] * B[nxk] = C[mxk]

        ROW1, COL1 = len(mat1), len(mat1[0])
        ROW2, COL2 = len(mat2), len(mat2[0])
        ans = [[0] * COL2 for _ in range(ROW1)]
        for i in range(ROW1):
            for j in range(COL1):
                if mat1[i][j]:
                    for k in range(COL2):
                        if mat2[j][k]:
                            ans[i][k] += mat1[i][j] * mat2[j][k]
        return ans

        return ans