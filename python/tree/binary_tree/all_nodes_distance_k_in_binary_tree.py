"""
863. All Nodes Distance K in Binary Tree
https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.



Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
Example 2:

Input: root = [1], target = 1, k = 3
Output: []


Constraints:

The number of nodes in the tree is in the range [1, 500].
0 <= Node.val <= 500
All the values Node.val are unique.
target is the value of one of the nodes in the tree.
0 <= k <= 1000

"""
from typing import List
from collections import defaultdict
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root: return None
        if not k:
            return [target.val]

        g = defaultdict(list)
        q = deque([root])
        while q:
            node = q.popleft()
            if node.left:
                q.append(node.left)
                g[node].append(node.left)
                g[node.left].append(node)
            if node.right:
                q.append(node.right)
                g[node].append(node.right)
                g[node.right].append(node)

        ans = []
        visit = set([target])
        q = deque([target])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if k == 0:
                    ans.append(node.val)
                for nei in g[node]:
                    if nei in visit: continue
                    q.append(nei)
                    visit.add(nei)
            k -= 1
        return ans


