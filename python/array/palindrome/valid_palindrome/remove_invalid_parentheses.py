"""
301. Remove Invalid Parentheses
https://leetcode.com/problems/remove-invalid-parentheses/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return a list of unique strings that are valid with the minimum number of removals. You may return the answer in any order.



Example 1:

Input: s = "()())()"
Output: ["(())()","()()()"]
Example 2:

Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]
Example 3:

Input: s = ")("
Output: [""]


Constraints:

1 <= s.length <= 25
s consists of lowercase English letters and parentheses '(' and ')'.
There will be at most 20 parentheses in s.
"""
from typing import List
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # ()())()
        #
        ans = set()
        longest = -1
        def dfs(l, r, i, combo):
            nonlocal longest
            if i >= len(s):
                if l == r:
                    if len(combo) > longest:
                        longest = len(combo)
                        ans.clear()
                        ans.add(''.join(combo))
                    elif len(combo) == longest:
                        ans.add(''.join(combo))
                return
            cur_char = s[i]
            if cur_char == '(':
                # case 1: take (
                combo.append(cur_char)
                dfs(l + 1, r, i + 1, combo)
                combo.pop()
                # case 2: not take (
                dfs(l, r, i + 1, combo)
            elif cur_char == ')':
                # case1 : not take )
                dfs(l, r, i + 1, combo)
                # case2: take )
                if l > r:
                    combo.append(cur_char)
                    dfs(l, r + 1, i + 1, combo)
                    combo.pop()
            else:# s[i] is letters
                combo.append(cur_char)
                dfs(l, r, i + 1, combo)
                combo.pop()
        dfs(0, 0, 0, [])
        return list(ans)
