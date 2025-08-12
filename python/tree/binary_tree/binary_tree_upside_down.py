"""
156. Binary Tree Upside Down
https://leetcode.com/problems/binary-tree-upside-down/description/?envType=company&envId=linkedin&favoriteSlug=linkedin-thirty-days

Given the root of a binary tree, turn the tree upside down and return the new root.

You can turn a binary tree upside down with the following steps:

The original left child becomes the new root.
The original root becomes the new right child.
The original right child becomes the new left child.

The mentioned steps are done level by level. It is guaranteed that every right node has a sibling (a left node with the same parent) and has no children.



Example 1:


Input: root = [1,2,3,4,5]
Output: [4,5,2,null,null,3,1]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]


Constraints:

The number of nodes in the tree will be in the range [0, 10].
1 <= Node.val <= 10
Every right node in the tree has a sibling (a left node that shares the same parent).
Every right node in the tree has no children.
"""

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # recursion
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        if not root.left: return root
        new_root = self.upsideDownBinaryTree(root.left) # go to the most left node, return this new root.
        root.left.left = root.right # reason why use root not new_root, because root keeps changing in recuriosn, new_root doesn't change, always the most left node
        root.left.right = root
        root.left = None
        root.right = None
        return new_root

    # iterative
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        prev = prev_right = None  # prev_right = pre.right
        cur = root
        while cur:
            tmp = cur.left
            cur.left = prev_right
            prev_right = cur.right
            cur.right = prev
            prev = cur
            cur = tmp
        return prev