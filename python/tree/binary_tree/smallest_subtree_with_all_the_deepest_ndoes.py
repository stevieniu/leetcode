"""
865. Smallest Subtree with all the Deepest Nodes
https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

Given the root of a binary tree, the depth of each node is the shortest distance to the root.

Return the smallest subtree such that it contains all the deepest nodes in the original tree.

A node is called the deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is a tree consisting of that node, plus the set of all descendants of that node.



Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation: We return the node with value 2, colored in yellow in the diagram.
The nodes coloured in blue are the deepest nodes of the tree.
Notice that nodes 5, 3 and 2 contain the deepest nodes in the tree but node 2 is the smallest subtree among them, so we return it.
Example 2:

Input: root = [1]
Output: [1]
Explanation: The root is the deepest node in the tree.
Example 3:

Input: root = [0,1,3,null,2]
Output: [2]
Explanation: The deepest node in the tree is 2, the valid subtrees are the subtrees of nodes 2, 1 and 0 but the subtree of node 2 is the smallest.


Constraints:

The number of nodes in the tree will be in the range [1, 500].
0 <= Node.val <= 500
The values of the nodes in the tree are unique.


Note: This question is the same as 1123: https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/
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
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None

        cache = collections.defaultdict(list)  # depth: [n1, n2, ...]
        q = collections.deque([root])
        depth = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                cache[depth].append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            depth += 1

        deepest_nodes = cache[max(cache.keys())]

        def dfs(root, p, q):
            if not root:
                return None
            if root in (p, q):
                return root
            l = dfs(root.left, p, q)
            r = dfs(root.right, p, q)
            if l and r:
                return root
            return l or r

        def divide_and_conquer(nodes):
            if len(nodes) == 0:
                return None
            elif len(nodes) == 1:
                return nodes[0]
            elif len(nodes) == 2:
                return dfs(root, nodes[0], nodes[1])
            else:
                n = len(nodes)
                r1 = divide_and_conquer(nodes[: n // 2])
                r2 = divide_and_conquer(nodes[n // 2:])
                if r1 and r2:
                    return divide_and_conquer([r1, r2])
                return r1 or r2

        return divide_and_conquer(deepest_nodes)

    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # check depth of left subtree and right subtree
        # if both depeth are equal, the common node is the ans
        # else recurse on the deeper subtree
        def dfs(node):
            if not node:
                return (0, None)
            ld, ln = dfs(node.left)
            rd, rn = dfs(node.right)
            depth = max(ld, rd) + 1
            ans = None
            if ld == rd:
                ans = node
            elif ld > rd:
                ans = ln
            else:
                ans = rn
            return (depth, ans)

        return dfs(root)[1]