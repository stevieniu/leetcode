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
    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     def merge_2_sorted_lists(list1, list2):
    #         if not list1 or not list2:
    #             return list1 if not list2 else list2
    #         head = ListNode(0)
    #         cur = head
    #         while list1 or list2:
    #             if list1 and list2:
    #                 if list1.val < list2.val:
    #                     cur.next = list1
    #                     list1 = list1.next
    #                     cur = cur.next
    #                 else:
    #                     cur.next = list2
    #                     cur = cur.next
    #                     list2 = list2.next
    #             else:
    #                 cur.next = list1 if list1 else list2
    #                 break
    #         return head.next

    #     if not lists or len(lists) == 0:
    #         return None

    #     while len(lists) > 1:
    #         merged_lists = []
    #         for i in range(0, len(lists), 2):
    #             l1 = lists[i]
    #             l2 = lists[i + 1] if i + 1 < len(lists) else None
    #             merged_lists.append(merge_2_sorted_lists(l1, l2))
    #         lists = merged_lists
    #     return lists[0]
    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     if not lists:
    #         return None
    #     if len(lists) == 1:
    #         return lists[0]
    #     def merge_two_lists(l1, l2):
    #         if not l1:
    #             return l2
    #         elif not l2:
    #             return l1
    #         elif l1.val < l2.val:
    #             l1.next = merge_two_lists(l1.next, l2)
    #             return l1
    #         else:
    #             l2.next = merge_two_lists(l1, l2.next)
    #             return l2
    #     l = lists[0]
    #     for i in range(1, len(lists)):
    #         l = merge_two_lists(l, lists[i])
    #     return l

    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     if not lists:
    #         return None

    #     def mergeLists(l1, l2):
    #         if not l1:
    #             return l2
    #         elif not l2:
    #             return l1

    #         curr = dummy = ListNode(0)

    #         while l1 or l2:
    #             if l1 and l2:
    #                 if l1.val < l2.val:
    #                     curr.next = l1
    #                     l1 = l1.next
    #                 else:
    #                     curr.next = l2
    #                     l2 = l2.next
    #             elif l1:
    #                 curr.next = l1
    #                 break
    #             else:
    #                 curr.next = l2
    #                 break
    #             curr = curr.next
    #         return dummy.next

    #     k = len(lists)
    #     l = lists[0]
    #     for i in range(1, k):
    #         l = mergeLists(l, lists[i])
    #     return l

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

