"""
23. https://leetcode.com/problems/merge-k-sorted-lists/description/

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.



Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []


Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
"""
from typing import Optional
from typing import List
import heapq
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def mergeLists(l1, l2):
            if not l1:
                return l2
            elif not l2:
                return l1

            if l1.val < l2.val:
                l1.next = mergeLists(l1.next, l2)
                return l1
            else:
                l2.next = mergeLists(l2.next, l1)
                return l2

        k = len(lists)
        l = lists[0]
        for i in range(1, k):
            l = mergeLists(l, lists[i])
        return l

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))

        curr = dummy = ListNode(0)

        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            curr.next = node
            curr = curr.next
            node = node.next
            if node:
                heapq.heappush(min_heap, (node.val, i, node))
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def merge(l1, l2):
            if not l1:
                return l2
            if not l2:
                return l1

            while l1 or l2:
                if l1 and l2:
                    if l1.val < l2.val:
                        l1.next = merge(l1.next, l2)
                        return l1
                    else:
                        l2.next = merge(l2.next, l1)
                        return l2
                elif l1:
                    return l1
                else:
                    return l2

        n = len(lists)
        if n == 1:
            return lists[0]
        elif n == 2:
            return merge(lists[0], lists[1])
        else:
            l, r = 0, n - 1
            m = l + (r - l) // 2
            left = self.mergeKLists(lists[0: m])
            right = self.mergeKLists(lists[m:])
            return merge(left, right)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # [1 -> 4 -> 5],
        #   cur
        # [1 -> 3 -> 4],
        #
        # [2 -> 6]
        #
        # [(1, 0, node1), (1, 1, node2), (2, 2, node3)]
        #
        if not lists:
            return None

        min_heap = []
        for i, node in enumerate(lists):  # i, listnode
            if node:
                heapq.heappush(min_heap, (node.val, i, node))
        curr = dummy = ListNode(0)
        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            curr.next = node
            curr = curr.next
            node = node.next
            if node:
                heapq.heappush(min_heap, (node.val, i, node))
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(l1, l2):
            dummy = cur = ListNode()
            while l1 or l2:
                if l1 and l2:
                    if l1.val < l2.val:
                        cur.next = ListNode(l1.val)
                        l1 = l1.next
                    else:
                        cur.next = ListNode(l2.val)
                        l2 = l2.next
                elif l1:
                    cur.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    cur.next = ListNode(l2.val)
                    l2 = l2.next
                cur = cur.next
            return dummy.next

        if not lists:
            return None
        elif len(lists) == 1:
            return lists[0]
        elif len(lists) == 2:
            return merge(lists[0], lists[1])
        else:
            m = len(lists) // 2
            l1 = self.mergeKLists(lists[:m])
            l2 = self.mergeKLists(lists[m:])
            return merge(l1, l2)

