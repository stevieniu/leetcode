"""
536. Construct Binary Tree from String
https://leetcode.com/problems/construct-binary-tree-from-string/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.



Example 1:


Input: s = "4(2(3)(1))(6(5))"
Output: [4,2,6,3,1,5]
Example 2:

Input: s = "4(2(3)(1))(6(5)(7))"
Output: [4,2,6,3,1,5,7]
Example 3:

Input: s = "-4(2(3)(1))(6(5)(7))"
Output: [-4,2,6,3,1,5,7]


Constraints:

0 <= s.length <= 3 * 104
s consists of digits, '(', ')', and '-' only.
All numbers in the tree have value at most than 230.
"""
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        # 4(2(3)(1))(6(5))
        #
        #
        if not s:
            return None
        stack = []
        i = 0
        while i < len(s):
            cur_char = s[i]
            if cur_char == '-':
                i += 1
                val = 0
                while i < len(s) and s[i].isdigit():
                    val = 10 * val + int(s[i])
                    i += 1
                i -= 1
                stack.append(TreeNode(-val))
            elif cur_char.isdigit():
                val = 0
                while i < len(s) and s[i].isdigit():
                    val = 10 * val + int(s[i])
                    i += 1
                i -= 1
                stack.append(TreeNode(val))
            elif cur_char == ')':
                node = stack.pop()
                if stack[-1].left:
                    stack[-1].right = node
                else:
                    stack[-1].left = node
            i += 1
        return stack[-1]