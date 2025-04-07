"""
101. https://leetcode.com/problems/symmetric-tree/description/

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).



Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false


Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100


Follow up: Could you solve it both recursively and iteratively?

"""
from typing import Optional
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # recursive
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        def dfs(l, r):
            if not l and not r:
                return True
            elif not l or not r:
                return False
            return l.val == r.val and dfs(l.left, r.right) and dfs(l.right, r.left)
        return dfs(root.left, root.right)

    # iterative
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = collections.deque([root, root])
        while q:
            tl, tr = q.popleft(), q.popleft()
            if not tl and not tr:
                continue
            elif not tl or not tr:
                return False
            elif tl.val != tr.val:
                return False
            q.append(tl.left)
            q.append(tr.right)
            q.append(tl.right)
            q.append(tr.left)
        return True