"""
254. Factor Combinations
https://leetcode.com/problems/factor-combinations/description/
Numbers can be regarded as the product of their factors.

For example, 8 = 2 x 2 x 2 = 2 x 4.
Given an integer n, return all possible combinations of its factors. You may return the answer in any order.

Note that the factors should be in the range [2, n - 1].



Example 1:

Input: n = 1
Output: []
Example 2:

Input: n = 12
Output: [[2,6],[3,4],[2,2,3]]
Example 3:

Input: n = 37
Output: []


Constraints:

1 <= n <= 107
"""
from typing import List
import math
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        def dfs(target, combo):
            if combo:  # because the combo must be at least two numbers
                ans.append(combo + [target])  # combo = [..., n] must be include n itself.
                # check if target can be splitted into smaller factors

            for i in range(2, int(math.sqrt(target)) + 1):
                # all factors in combo are in asceding order, n1 * n2 * ...* n_last == target
                # so n_last * n_last <= target, therefore n_last <= sqrt(target)
                if target % i == 0:  # i to be factor of target, target % i == 0
                    if combo and i < combo[-1]: continue  # avoid duplicate
                    combo.append(i)
                    dfs(target // i, combo)
                    combo.pop()

        ans = []
        dfs(n, [])
        return ans
