"""
863. All Nodes Distance K in Binary Tree
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
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not k:
            return [target.val]

        q = collections.deque([root])
        graph = collections.defaultdict(list)
        while q:
            node = q.popleft()
            if node.left:
                q.append(node.left)
                graph[node].append(node.left)
                graph[node.left].append(node)
            if node.right:
                q.append(node.right)
                graph[node].append(node.right)
                graph[node.right].append(node)

        q1 = collections.deque([target])
        visit = set([target])
        distance = 0
        res = []
        while q1:
            lenQ = len(q1)
            for _ in range(lenQ):
                node = q1.popleft()
                if distance == k:
                    res.append(node.val)
                for n in graph[node]:
                    if n not in visit:
                        q1.append(n)
                        visit.add(n)
            distance += 1
        return res
