"""
270. Closest Binary Search Tree Value
https://leetcode.com/problems/closest-binary-search-tree-value/description/
Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target. If there are multiple answers, print the smallest.



Example 1:


Input: root = [4,2,5,1,3], target = 3.714286
Output: 4
Example 2:

Input: root = [1], target = 4.428571
Output: 1


Constraints:

The number of nodes in the tree is in the range [1, 104].
0 <= Node.val <= 109
-109 <= target <= 109
"""
from typing import Optional
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        min_diff = float('inf')
        res = root.val
        while root:
            if abs(root.val - target) < min_diff:
                min_diff = abs(root.val - target)
                res = root.val
            elif abs(root.val - target) == min_diff:
                res = min(res, root.val)

            if root.val == target:
                return root.val
            elif root.val < target:
                root = root.right
            else:
                root = root.left
        return res

    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        min_diff = float('inf')
        target_node = root
        curr = root
        while curr:
            diff = abs(curr.val - target)
            if diff == 0:
                return curr.val

            if diff < min_diff:
                min_diff = diff
                target_node = curr
            elif diff == min_diff:
                if curr.val < target_node.val:
                    target_node = curr
            if target < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return target_node.val

    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        ans = float('inf')
        min_diff = float('inf')

        def dfs(node):
            nonlocal ans, min_diff
            if not node:
                return
            dfs(node.left)
            diff = abs(node.val - target)
            if diff < min_diff:
                min_diff = diff
                ans = node.val
            dfs(node.right)

        dfs(root)
        return ans
