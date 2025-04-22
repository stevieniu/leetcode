"""
251. Flatten 2D Vector
https://leetcode.com/problems/flatten-2d-vector/description/

Design an iterator to flatten a 2D vector. It should support the next and hasNext operations.

Implement the Vector2D class:

Vector2D(int[][] vec) initializes the object with the 2D vector vec.
next() returns the next element from the 2D vector and moves the pointer one step forward. You may assume that all the calls to next are valid.
hasNext() returns true if there are still some elements in the vector, and false otherwise.


Example 1:

Input
["Vector2D", "next", "next", "next", "hasNext", "hasNext", "next", "hasNext"]
[[[[1, 2], [3], [4]]], [], [], [], [], [], [], []]
Output
[null, 1, 2, 3, true, true, 4, false]

Explanation
Vector2D vector2D = new Vector2D([[1, 2], [3], [4]]);
vector2D.next();    // return 1
vector2D.next();    // return 2
vector2D.next();    // return 3
vector2D.hasNext(); // return True
vector2D.hasNext(); // return True
vector2D.next();    // return 4
vector2D.hasNext(); // return False


Constraints:

0 <= vec.length <= 200
0 <= vec[i].length <= 500
-500 <= vec[i][j] <= 500
At most 105 calls will be made to next and hasNext.


Follow up: As an added challenge, try to code it using only iterators in C++ or iterators in Java.
"""
from typing import List


class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.i = 0
        self.j = 0

    def next(self) -> int:
        self.hasNext()
        val = self.vec[self.i][self.j]
        self.j += 1
        return val

    def hasNext(self) -> bool:
        while self.i < len(self.vec):  # in case vec[self.i] is empty, then go to next row
            if self.j < len(
                    self.vec[self.i]):  # if this row is valid, then directly return row, otherwise move to next row
                return True
            self.i += 1  # when i + 1, move to next row, this row could be empty, that's why use while inestad of if
            self.j = 0
        return False

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()