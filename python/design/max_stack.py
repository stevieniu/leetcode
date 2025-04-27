"""
716. Max Stack
https://leetcode.com/problems/max-stack/description/?envType=company&envId=linkedin&favoriteSlug=linkedin-thirty-days

Design a max stack data structure that supports the stack operations and supports finding the stack's maximum element.

Implement the MaxStack class:

MaxStack() Initializes the stack object.
void push(int x) Pushes element x onto the stack.
int pop() Removes the element on top of the stack and returns it.
int top() Gets the element on the top of the stack without removing it.
int peekMax() Retrieves the maximum element in the stack without removing it.
int popMax() Retrieves the maximum element in the stack and removes it. If there is more than one maximum element, only remove the top-most one.
You must come up with a solution that supports O(1) for each top call and O(logn) for each other call.



Example 1:

Input
["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]
[[], [5], [1], [5], [], [], [], [], [], []]
Output
[null, null, null, null, 5, 5, 1, 5, 1, 5]

Explanation
MaxStack stk = new MaxStack();
stk.push(5);   // [5] the top of the stack and the maximum number is 5.
stk.push(1);   // [5, 1] the top of the stack is 1, but the maximum is 5.
stk.push(5);   // [5, 1, 5] the top of the stack is 5, which is also the maximum, because it is the top most one.
stk.top();     // return 5, [5, 1, 5] the stack did not change.
stk.popMax();  // return 5, [5, 1] the stack is changed now, and the top is different from the max.
stk.top();     // return 1, [5, 1] the stack did not change.
stk.peekMax(); // return 5, [5, 1] the stack did not change.
stk.pop();     // return 1, [5] the top of the stack and the max element is now 5.
stk.top();     // return 5, [5] the stack did not change.


Constraints:

-107 <= x <= 107
At most 105 calls will be made to push, pop, top, peekMax, and popMax.
There will be at least one element in the stack when pop, top, peekMax, or popMax is called.
"""
from sortedcontainers import SortedDict


class Node:
    def __init__(self, key=0):
        self.key = key
        self.prev = None
        self.next = None


class MaxStack:

    def __init__(self):
        self.left = Node()
        self.right = Node()
        self.cache = SortedDict()  # {value: [node1, node2,...]}
        self.left.next = self.right
        self.right.prev = self.left

    def push(self, x: int) -> None:
        node = Node(x)
        self.insert(node)
        if x in self.cache:
            self.cache[x].append(node)
        else:
            self.cache[x] = []
            self.cache[x].append(node)

    def pop(self) -> int:
        if self.left.next == self.right:  # empty stack
            return -1
        node = self.right.prev
        self.remove(node)
        if len(self.cache[node.key]) == 1:  # there is only one node for the key, once pop this node, delete this key
            del self.cache[node.key]
        else:
            self.cache[node.key].remove(node)
        return node.key

    def top(self) -> int:
        if self.left.next == self.right:  # empty stack
            return -1
        node = self.right.prev
        return node.key

    def peekMax(self) -> int:
        key, node_lst = self.cache.peekitem()
        return key

    def popMax(self) -> int:
        key, node_lst = self.cache.peekitem()
        last_node = node_lst[-1]
        if len(self.cache[key]) == 1:
            del self.cache[key]
        else:
            self.cache[key].remove(last_node)
        self.remove(last_node)
        return key

    def insert(self, node):  # insert just before right end
        prev, next = self.right.prev, self.right
        node.prev, node.next = prev, next
        prev.next = node
        next.prev = node

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()


# [5, 1, 5, 4, 0, 7]
#
# left <-> 5 <-> 1 <-> 5 <-> right
#   {1: [N1], 5: [N5, N5]}





