"""
61. Rotate List
https://leetcode.com/problems/rotate-list/description/?envType=company&envId=linkedin&favoriteSlug=linkedin-three-months

Given the head of a linked list, rotate the list to the right by k places.



Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]


Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
"""

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head

        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        dummy = ListNode(0, head)
        fast = slow = dummy
        k %= length
        for _ in range(k):
            fast = fast.next

        for _ in range(length - k):
            fast = fast.next  # fast points to the last node
            slow = slow.next

        fast.next = dummy.next
        dummy.next = slow.next
        slow.next = None
        return dummy.next


