"""
432. All O`one Data Structure
https://leetcode.com/problems/all-oone-data-structure/description/?envType=company&envId=linkedin&favoriteSlug=linkedin-thirty-days

Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

Implement the AllOne class:

AllOne() Initializes the object of the data structure.
inc(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1.
dec(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it from the data structure. It is guaranteed that key exists in the data structure before the decrement.
getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".
Note that each function must run in O(1) average time complexity.



Example 1:

Input
["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
[[], ["hello"], ["hello"], [], [], ["leet"], [], []]
Output
[null, null, null, "hello", "hello", null, "hello", "leet"]

Explanation
AllOne allOne = new AllOne();
allOne.inc("hello");
allOne.inc("hello");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "hello"
allOne.inc("leet");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "leet"


Constraints:

1 <= key.length <= 10
key consists of lowercase English letters.
It is guaranteed that for each call to dec, key is existing in the data structure.
At most 5 * 104 calls will be made to inc, dec, getMaxKey, and getMinKey.
"""


class Node:
    def __init__(self, freq=-1):
        self.freq = freq
        self.keys = set()
        self.prev = None
        self.next = None


class AllOne:

    def __init__(self):
        self.cache = {}  # word: node
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left

    def inc(self, key: str) -> None:
        if key not in self.cache:
            if self.left.next == self.right or self.left.next.freq > 1:
                node = Node(1)
                node.keys.add(key)
                self.insert_node(node, self.left, self.left.next)
                self.cache[key] = node
            else:
                self.left.next.keys.add(key)
                self.cache[key] = self.left.next
        else:
            curr = self.cache[key]
            freq = curr.freq
            curr.keys.remove(key)
            if curr.next == self.right or curr.next.freq != freq + 1:
                node = Node(freq + 1)
                node.keys.add(key)
                self.insert_node(node, curr, curr.next)
                self.cache[key] = node
            else:  # move key to the next node
                curr.next.keys.add(key)
                self.cache[key] = curr.next
            if len(curr.keys) == 0:
                self.remove_node(curr)

    def dec(self, key: str) -> None:
        if key not in self.cache:  # the key doesn't exist, no action required
            return
        curr = self.cache[key]
        curr.keys.remove(key)
        freq = curr.freq
        if freq == 1:
            del self.cache[key]
        else:
            # move the key to the node of freq - 1
            prev = curr.prev
            if prev == self.left or prev.freq != curr.freq - 1:  # create new node with freq - 1
                node = Node(freq - 1)
                node.keys.add(key)
                self.insert_node(node, prev, curr)
                self.cache[key] = node
            else:  # move the key to previous node
                prev.keys.add(key)
                self.cache[key] = prev
        if len(curr.keys) == 0:  # there are no words with this freq, no need for this node
            self.remove_node(curr)

    def getMaxKey(self) -> str:
        if self.left.next == self.right:
            return ''
        return next(iter(self.right.prev.keys))

    def getMinKey(self) -> str:
        if self.left.next == self.right:
            return ''
        return next(
            iter(self.left.next.keys)
        )

    def insert_node(self, node, prev, next):
        node.prev, node.next = prev, next
        prev.next = node
        next.prev = node

    def remove_node(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()