"""
234. Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

Given the head of a singly linked list, return true if it is a palindrome or false otherwise.



Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false


Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9


Follow up: Could you do it in O(n) time and O(1) space?
"""

from  typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        while slow:
            succesor = slow.next
            slow.next = prev
            prev = slow
            slow = succesor
        # prev is the head of the reversed 2nd half linkedlist
        curr = head
        while curr and prev:
            if curr.val != prev.val:
                return False
            curr = curr.next
            prev = prev.next
        return True

