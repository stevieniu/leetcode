"""
129. Sum Root to Leaf Numbers
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.



Example 1:


Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:


Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.


Constraints:

The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 9
The depth of the tree will not exceed 10.
"""

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, path):
            nonlocal total
            if not node:
                return

            path.append(node.val)
            if not node.left and not node.right:
                number = 0
                for d in path:
                    number = 10 * number + d
                total += number
            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()

        total = 0
        dfs(root, [])
        return total

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        numbers = []

        def dfs(node, num):
            if not node:
                return
            if not node.left and not node.right:
                numbers.append(10 * num + int(node.val))
            dfs(node.left, 10 * num + int(node.val))

            dfs(node.right, 10 * num + int(node.val))

        dfs(root, 0)
        return sum(numbers)