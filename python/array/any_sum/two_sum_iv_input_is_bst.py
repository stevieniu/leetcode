"""
653. Two Sum IV - Input is a BST
https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/

Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.



Example 1:


Input: root = [5,3,6,2,4,null,7], k = 9
Output: true
Example 2:


Input: root = [5,3,6,2,4,null,7], k = 28
Output: false


Constraints:

The number of nodes in the tree is in the range [1, 104].
-104 <= Node.val <= 104
root is guaranteed to be a valid binary search tree.
-105 <= k <= 105
"""
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nums = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            nums.append(node.val)
            dfs(node.right)
        dfs(root)
        l, r = 0, len(nums) - 1
        while l < r :
            sum = nums[l] + nums[r]
            if sum == k: return True
            elif sum > k: r -= 1
            else: l += 1
        return False

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        data_set = set()
        def dfs(node): # is there pair of nodes in the tree whose root is node
            if not node:
                return False
            if k - node.val in data_set:
                return True
            data_set.add(node.val)
            return dfs(node.left) or dfs(node.right)
        return dfs(root)