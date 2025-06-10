"""
1944. Number of Visible People in a Queue
https://leetcode.com/problems/number-of-visible-people-in-a-queue/description/?envType=company&envId=linkedin&favoriteSlug=linkedin-three-months

There are n people standing in a queue, and they numbered from 0 to n - 1 in left to right order. You are given an array heights of distinct integers where heights[i] represents the height of the ith person.

A person can see another person to their right in the queue if everybody in between is shorter than both of them. More formally, the ith person can see the jth person if i < j and min(heights[i], heights[j]) > max(heights[i+1], heights[i+2], ..., heights[j-1]).

Return an array answer of length n where answer[i] is the number of people the ith person can see to their right in the queue.



Example 1:



Input: heights = [10,6,8,5,11,9]
Output: [3,1,2,1,1,0]
Explanation:
Person 0 can see person 1, 2, and 4.
Person 1 can see person 2.
Person 2 can see person 3 and 4.
Person 3 can see person 4.
Person 4 can see person 5.
Person 5 can see no one since nobody is to the right of them.
Example 2:

Input: heights = [5,1,2,3,10]
Output: [4,1,1,1,0]


Constraints:

n == heights.length
1 <= n <= 105
1 <= heights[i] <= 105
All the values of heights are unique.
"""
from typing import List
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        # 5,1,2,3,10
        # i
        #stack = [10, 5] => decesing monotonic stack .  | ans = [4, 1, 1, 1, 0]  4
        stack = []
        N = len(heights)
        ans = [0] * N
        for i in range(N - 1, -1, -1):
            cnt = 0
            if not stack: # empty stack, push current height, cnt is 0
                stack.append(heights[i])
            else:
                # compare current height with top stack, if current height is smaller or equal, push to stack, otherwise pop from stack and keep comparing
                while stack and stack[-1] < heights[i]:
                    stack.pop()
                    cnt += 1
                # now stack is either empty or stack top is heigher than current height
                if stack:
                    cnt += 1
                stack.append(heights[i])
                ans[i] = cnt

        return ans