"""
314. Binary Tree Vertical Order Traversal
https://leetcode.com/problems/binary-tree-vertical-order-traversal/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Example 2:


Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]
Example 3:


Input: root = [1,2,3,4,10,9,11,null,5,null,null,null,null,null,null,null,6]
Output: [[4],[2,5],[1,10,9,6],[3],[11]]


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""
from typing import Optional
from typing import List
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        q = collections.deque([(root, 0)]) # (node, col)
        min_col, max_col = 0, 0
        col_map = collections.defaultdict(list) # col: [values]
        while q:
            node, col = q.popleft()
            min_col, max_col = min(min_col, col), max(max_col, col)
            col_map[col].append(node.val)
            if node.left:
                q.append((node.left, col - 1))
            if node.right:
                q.append((node.right, col + 1))
        return [col_map[key] for key in range(min_col, max_col + 1)]