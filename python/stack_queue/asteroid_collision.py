"""
735. Asteroid Collision
https://leetcode.com/problems/asteroid-collision/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

We are given an array asteroids of integers representing asteroids in a row. The indices of the asteriod in the array represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.



Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.


Constraints:

2 <= asteroids.length <= 104
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0
"""
from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #-10,2,-5
        #
        stack = []
        for w in asteroids:
            while stack and stack[-1] > 0 and w < 0 and abs(stack[-1]) < abs(w):
                stack.pop()
            # after while processing, only below cases
            # 1) stack is empty, then push
            # 2) stack[-1] and w are the same direction, push
            # 3) stack[-1] is negative, w is positive, push
            # 4) staci[-1] is positve and w is negative, and stack[-1] > w, dont push
            # 5) stack[-1] is positive, and w is negative and stack[-1] == w, pop and don't push
            if stack and stack[-1] > 0 and w < 0 and  abs(stack[-1]) > abs(w): continue
            elif stack and stack[-1] > 0 and w < 0  and abs(stack[-1]) == abs(w):
                stack.pop()
                continue
            stack.append(w)
        return stack