"""
199. Binary Tree Right Side View
https://leetcode.com/problems/binary-tree-right-side-view/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.



Example 1:

Input: root = [1,2,3,null,5,null,4]

Output: [1,3,4]

Explanation:



Example 2:

Input: root = [1,2,3,4,null,null,null,5]

Output: [1,3,4,5]

Explanation:



Example 3:

Input: root = [1,null,3]

Output: [1,3]

Example 4:

Input: root = []

Output: []



Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

"""

from typing import Optional
from typing import List
# Definition for a binary tree node.
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    #     if not root:
    #         return []

    #     res = []
    #     q = collections.deque([root])
    #     while q:
    #         n = len(q)
    #         res.append(q[- 1].val)
    #         for _ in range(n):
    #             node = q.popleft()
    #             if node.left:
    #                 q.append(node.left)
    #             if node.right:
    #                 q.append(node.right)

    #     return res

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = collections.deque([root])
        res = []
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                # first node in the q is the most right node
                if i == 0:
                    res.append(node.val)
                # append right child to the queue first, then left child
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)

        return res

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        q = collections.deque([root])
        levels = []
        while q:
            lvl = []
            for _ in range(len(q)):
                node = q.popleft()
                lvl.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            levels.append(lvl.copy())
        return [lvl[-1] for lvl in levels]