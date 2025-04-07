"""
22. https://leetcode.com/problems/generate-parentheses/description/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]


Constraints:

1 <= n <= 8
"""

from typing import List
class Solution:
    #     def generateParenthesis(self, n: int) -> List[str]:
    #         ans = []
    #         def dfs(l, r, combo):
    #             if l == n and r == n:
    #                 ans.append(combo)
    #                 return

    #             if l < n:
    #                 dfs(l + 1, r, combo + '(')
    #             if r < l:
    #                 dfs(l, r + 1, combo + ')')
    #         dfs(0, 0, '')
    #         return ans

    # time complex O(2^n), space complex O(n)
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        combo = []

        def dfs(l, r):
            if l == n and r == n:
                ans.append(''.join(combo))
                return
            if l < n:
                combo.append('(')
                dfs(l + 1, r)
                combo.pop()
            if r < l:
                combo.append(')')
                dfs(l, r + 1)
                combo.pop()

        dfs(0, 0)
        return ans
Solution().generateParenthesis(2)