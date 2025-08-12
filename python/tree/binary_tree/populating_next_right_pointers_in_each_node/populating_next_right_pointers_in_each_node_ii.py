"""
117. Populating Next Right Pointers in Each Node II
https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.



Example 1:


Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
Example 2:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 6000].
-100 <= Node.val <= 100


Follow-up:

You may only use constant extra space.
The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
import collections
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        curr = root # curr: one level above the working level
        leftmost = nxt = None # the actual working level, leftmost points to left most node, doesn't move; nxt move horisontally
        while curr: # curr move downward
            while curr: # curr moving horisontally, when curr is None, means reach the end of this level, should move to next level
                if curr.left:
                    if not leftmost: # leftmost not set, means first time on the next level, starting from leftmost
                        leftmost = curr.left
                        nxt = leftmost
                    else: # nxt is already in the move
                        #         cur
                        #    1     2
                        #    / \   /
                    # leftmost nxt
                        nxt.next = curr.left
                        nxt = nxt.next
                if curr.right:
                    if not leftmost: # leftmost not set, means first time on the next level, starting from leftmost, curr doesn't have left subtree
                        leftmost = curr.right
                        nxt = leftmost
                    else:# nxt is already in the move
                        #         cur
                        #    1     2
                        #    / \   \
                    # leftmost nxt
                        nxt.next = curr.right
                        nxt = nxt.next
                curr = curr.next
            curr = leftmost
            leftmost = nxt = None
        return root

    def connect(self, root: 'Node') -> 'Node':
        if not root: return None
        q = collections.deque([root])
        while q:
            lvl = []
            for _ in range(len(q)):
                node = q.popleft()
                lvl.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            for i in range(len(lvl) - 1):
                lvl[i].next = lvl[i + 1]
        return root





