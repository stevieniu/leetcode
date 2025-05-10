"""
272. Closest Binary Search Tree Value II
Given the root of a binary search tree, a target value, and an integer k, return the k values in the BST that are closest to the target. You may return the answer in any order.

You are guaranteed to have only one unique set of k values in the BST that are closest to the target.



Example 1:


Input: root = [4,2,5,1,3], target = 3.714286, k = 2
Output: [4,3]
Example 2:

Input: root = [1], target = 0.000000, k = 1
Output: [1]


Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 104.
0 <= Node.val <= 109
-109 <= target <= 109


Follow up: Assume that the BST is balanced. Could you solve it in less than O(n) runtime (where n = total nodes)?
"""
from typing import Optional
from typing import List
import heapq
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        # 1 2 3 4 5 | 3.714    |3.714 - 5| =
        #         i
        # [ 3, 4]
        arr = []
        def dfs(node): #  inorder traversal
            if not node:
                return
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
        dfs(root)
        q = collections.deque([])
        for num in arr:
            if len(q) < k:
                q.append(num)
            else:
                if abs(num - target) < abs(q[0] - target):
                    q.popleft() # num is the new numbet to be in the queue
                    q.append(num) # discard the first element in the queue
                else:
                    break
        return list(q)

    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        q = collections.deque()

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            if len(q) < k:
                q.append(node.val)
            else:
                if abs(q[0] - target) > abs(node.val - target):
                    q.popleft()
                    q.append(node.val)
                else:
                    return
            dfs(node.right)

        dfs(root)
        return list(q)

    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        max_heap = []  # abs diff

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            diff = abs(node.val - target)
            if len(max_heap) == k:
                if diff < -max_heap[0][0]:
                    heapq.heappushpop(max_heap, (-diff, node.val))
            else:
                heapq.heappush(max_heap, (-diff, node.val))
            dfs(node.right)

        dfs(root)
        return [item[1] for item in max_heap]

    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        ans = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)

        dfs(root)
        # ans = [1, 2, 3, 4, 5]
        l, r = 0, len(ans) - k  # m will be the left boundry of the window
        while l < r:
            m = l + (r - l) // 2
            if ans[m + k] - target < target - ans[m]:  # ans[m + k] is the number just out of right boudry of the window
                l = m + 1  # need to include ans[m + k], means move the window right
            else:
                r = m

        return ans[l: l + k]

        # O(log(n))
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        # 1 2 3 4 5 6 | root= 4, target = 3.7, pred = [1, 2, 3], succsor = [4, 5 ,6]
        #

        def init_predssor(node):
            while node:
                if node.val == target:
                    predssor.append(node)
                    return
                elif node.val < target:  # the node is predssor
                    predssor.append(node)
                    node = node.right
                else:
                    node = node.left

        def init_succsor(node):
            while node:
                if node.val > target:
                    succssor.append(node)
                    node = node.left
                else:
                    node = node.right

        def get_predssor(node):
            pred = node.left
            while pred:
                predssor.append(pred)
                pred = pred.right

        def get_successor(node):
            suc = node.right
            while suc:
                succssor.append(suc)
                suc = suc.left

        predssor, succssor = [], []
        # initialize predssor and succssor
        init_predssor(root)
        init_succsor(root)

        ans = []
        while k > 0:
            k -= 1
            if not predssor:  # all numbers from succssor
                node = succssor.pop()
                ans.append(node.val)
                get_successor(node)
            elif not succssor:  # all numbers from predssor
                node = predssor.pop()
                ans.append(node.val)
                get_predssor(node)
            else:
                pred = predssor[-1]
                suc = succssor[-1]
                if abs(pred.val - target) <= abs(suc.val - target):
                    node = predssor.pop()
                    ans.append(node.val)
                    get_predssor(node)
                else:
                    node = succssor.pop()
                    ans.append(node.val)
                    get_successor(node)

        return ans