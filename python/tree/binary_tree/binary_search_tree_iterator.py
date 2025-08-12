"""
173. Binary Search Tree Iterator
https://leetcode.com/problems/binary-search-tree-iterator/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.



Example 1:


Input
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
Output
[null, 3, 7, true, 9, true, 15, true, 20, false]

Explanation
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // return 3
bSTIterator.next();    // return 7
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 9
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 15
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 20
bSTIterator.hasNext(); // return False


Constraints:

The number of nodes in the tree is in the range [1, 105].
0 <= Node.val <= 106
At most 105 calls will be made to hasNext, and next.


Follow up:

Could you implement next() and hasNext() to run in average O(1) time and use O(h) memory, where h is the height of the tree?
"""
from typing import Optional
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.cur = root
        self.stack = []
        while self.cur:
            self.stack.append(self.cur)
            self.cur = self.cur.left

    def next(self) -> int:
        if not self.stack: return -1
        self.cur = self.stack.pop()
        tmp = self.cur.right
        while tmp:
            self.stack.append(tmp)
            tmp = tmp.left

        return self.cur.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.stack = []
        curr = root
        while curr:
            self.stack.append(curr)
            curr = curr.left

    def next(self) -> int:
        if not self.stack:
            return None
        tmp = self.stack.pop()
        if tmp.right:
            curr = tmp.right
            while curr:
                self.stack.append(curr)
                curr = curr.left
        return tmp.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()