"""
671. Second Minimum Node In a Binary Tree
https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/description/

Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.





Example 1:


Input: root = [2,2,5,null,null,5,7]
Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.
Example 2:


Input: root = [2,2,2]
Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.


Constraints:

The number of nodes in the tree is in the range [1, 25].
1 <= Node.val <= 231 - 1
root.val == min(root.left.val, root.right.val) for each internal node of the tree.
"""

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root or not root.left: return -1
        if root.left.val == root.right.val:
            l_sec_min = self.findSecondMinimumValue(root.left)
            r_sec_min = self.findSecondMinimumValue(root.right)
            if l_sec_min != -1 and r_sec_min != -1:
                return min(l_sec_min, r_sec_min)
            else:
                return l_sec_min if l_sec_min != -1 else r_sec_min
        elif root.val < root.right.val:  # root.val == root.left.val
            # don't need to seach root.righjt
            l_sec_min = self.findSecondMinimumValue(root.left)
            if l_sec_min == -1:
                return root.right.val
            return min(root.right.val, l_sec_min)
        elif root.val < root.left.val:
            # don't need to seach root.left
            r_sec_min = self.findSecondMinimumValue(root.right)
            if r_sec_min == -1:
                return root.left.val
            return min(root.left.val, r_sec_min)

