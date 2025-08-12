"""
426. Convert Binary Search Tree to Sorted Doubly Linked List
https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.



Example 1:



Input: root = [4,2,5,1,3]


Output: [1,2,3,4,5]

Explanation: The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.

Example 2:

Input: root = [2,1,3]
Output: [1,2,3]


Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
All the values of the tree are unique.
"""

# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """
        node(1).right -> node(2)
        node(1)  <- node(2).left
        left pointer points to smaller value
        right pointer points to larger value
        """
        if not root: return None

        def dfs(node):
            nonlocal last, first
            if not node:
                return

            dfs(node.left)
            # reached the most left node
            if not last:  # last is not set, means the current node is the first node
                first = node
            else:
                # before last is reset, last is the node previously visited,
                # the value of last must be smaller than current
                last.right = node
                node.left = last
            last = node
            dfs(node.right)

        first, last = None, None

        dfs(root)
        first.left = last
        last.right = first
        return first

    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        stack = []
        curr = root

        first, last = None, None
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if not last:
                first = curr
            else:
                curr.left = last
                last.right = curr
            last = curr
            curr = curr.right

        first.left = last
        last.right = first
        return first

    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        path = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            path.append(node.val)
            dfs(node.right)

        dfs(root)
        head = Node(0)
        tail = Node(0)
        head.right = tail
        tail.left = head
        cur = head
        for num in path:
            node = Node(num)
            prev, next = cur, cur.right
            node.left, node.right = prev, next
            prev.right = node
            next.left = node
            cur = cur.right
        # cur at tail
        # head <> 1 <> 2 <> tail
        real_head = head.right
        real_tail = tail.left
        real_head.left = real_tail
        real_tail.right = real_head
        return real_head


    # In place
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        first = last = None

        def dfs(node):
            nonlocal first, last
            if not node:
                return
            dfs(node.left)
            if not first:
                first = node
            if last:
                last.right = node
                node.left = last
            last = node

            dfs(node.right)

        dfs(root)
        first.left = last
        last.right = first
        return first
