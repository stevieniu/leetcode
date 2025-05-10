"""
366. Find Leaves of Binary Tree
https://leetcode.com/problems/find-leaves-of-binary-tree/description/?envType=company&envId=linkedin&favoriteSlug=linkedin-thirty-days
Given the root of a binary tree, collect a tree's nodes as if you were doing this:

Collect all the leaf nodes.
Remove all the leaf nodes.
Repeat until the tree is empty.


Example 1:


Input: root = [1,2,3,4,5]
Output: [[4,5,3],[2],[1]]
Explanation:
[[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each level it does not matter the order on which elements are returned.
Example 2:

Input: root = [1]
Output: [[1]]


Constraints:

The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
      depth for each node is marked with (). depth of node = max(left depth, right depth) + 1
        1 (3)
      /   \
      2(2) 3 (1)
    /  \
   4(1) 5(1)
      """

from typing import Optional
from typing import List
import collections
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(node):  # the depth of current node
            if not node:  # None node depth is 0
                return 0

            l_depth = dfs(node.left)
            r_depth = dfs(node.right)
            curr_depth = max(l_depth, r_depth) + 1
            node_to_depth[curr_depth].append(node.val)
            return curr_depth

        node_to_depth = collections.defaultdict(list)
        dfs(root)
        return [item for k, item in node_to_depth.items()]


