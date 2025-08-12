"""
111. Minimum Depth of Binary Tree
https://leetcode.com/problems/minimum-depth-of-binary-tree/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5


Constraints:

The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000

"""
import collections
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = collections.deque([root])
        step = 0
        while q:
            step += 1
            for _ in range(len(q)):
                node = q.popleft()
                if not node.left and not node.right:
                    return step
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node, cur_depth):
            nonlocal min_depth
            if not node:
                return

            if not node.left and not node.right:
                min_depth = min(min_depth, cur_depth + 1)
            dfs(node.left, cur_depth + 1)
            dfs(node.right, cur_depth + 1)

        min_depth = float('inf')
        dfs(root, 0)
        return min_depth if min_depth != float('inf') else 0