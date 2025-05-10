"""
50. Pow(x, n)
https://leetcode.com/problems/powx-n/description/?envType=company&envId=linkedin&favoriteSlug=linkedin-thirty-days
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).



Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25


Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
n is an integer.
Either x is not zero or n > 0.
-104 <= xn <= 104
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        is_negative = True if n < 0 else False
        n = abs(n)
        def dfs(x, n):
            if n == 0:
                return 1
            elif n == 1:
                return x
            val = dfs(x, n // 2)
            res = val * val if n % 2 == 0 else \
                val * val * x
            return res
        res = dfs(x, n)
        return 1 / res if is_negative else res