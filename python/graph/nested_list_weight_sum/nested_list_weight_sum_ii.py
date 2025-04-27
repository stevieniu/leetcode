"""
364. Nested List Weight Sum II

https://leetcode.com/problems/nested-list-weight-sum-ii/description/?envType=company&envId=linkedin&favoriteSlug=linkedin-thirty-days

You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists.

The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth. Let maxDepth be the maximum depth of any integer.

The weight of an integer is maxDepth - (the depth of the integer) + 1.

Return the sum of each integer in nestedList multiplied by its weight.



Example 1:


Input: nestedList = [[1,1],2,[1,1]]
Output: 8
Explanation: Four 1's with a weight of 1, one 2 with a weight of 2.
1*1 + 1*1 + 2*2 + 1*1 + 1*1 = 8
Example 2:


Input: nestedList = [1,[4,[6]]]
Output: 17
Explanation: One 1 at depth 3, one 4 at depth 2, and one 6 at depth 1.
1*3 + 4*2 + 6*1 = 17


Constraints:

1 <= nestedList.length <= 50
The values of the integers in the nested list is in the range [-100, 100].
The maximum depth of any integer is less than or equal to 50.
There are no empty lists.

"""


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """
from typing import List
import collections
class Solution:

    # dfs
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        max_depth = self.get_max_level(nestedList)

        def dfs(nestedList, depth):
            ans = 0
            for lst in nestedList:
                if lst.isInteger():
                    ans += depth * lst.getInteger()
                else:
                    ans += dfs(lst.getList(), depth - 1)
            return ans

        return dfs(nestedList, max_depth)

    def get_max_level(self, nestedList):  # max level for nestedList
        depth = 0
        for lst in nestedList:
            if not lst.isInteger():  # it is nested list
                depth = max(depth, self.get_max_level(lst.getList()))
        return depth + 1  # plus one is because to include the current depth


    # bfs
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        # [1,[4,[6]]]
        #  4 * 1 + 4 * 4 + 6 * 4 = (1 + 4 + 6) * 4
        #  3 * 1 + 2 * 4 + 1 * 6 = (1 + 4 + 6) * 4 - (1 * 1 + 2 * 4 + 3 * 6)

        # (1 * 1 + 2 * 4 + 3 * 6) => it is nested list weight sum I
        q = collections.deque(nestedList)
        sum = 0  # (integer1 + integer2 + ...) * maxDepth
        extra = 0  # it is nested list weight sum I
        depth = 1
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr.isInteger():
                    extra += curr.getInteger() * depth
                    sum += curr.getInteger()
                else:
                    for node in curr.getList():
                        q.append(node)
            depth += 1
        sum *= depth
        return sum - extra