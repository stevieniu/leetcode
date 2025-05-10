"""
658. Find K Closest Elements
https://leetcode.com/problems/find-k-closest-elements/description/?envType=company&envId=linkedin&favoriteSlug=linkedin-thirty-days

Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b


Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3

Output: [1,2,3,4]

Example 2:

Input: arr = [1,1,2,3,4,5], k = 4, x = -1

Output: [1,1,2,3]



Constraints:

1 <= k <= arr.length
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104
"""
from typing import List
import collections
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # looking for a window sized k, the left boudary of the window is mid,
        # right boudary of the windor is mid + k - 1
        """
        0 1 2 3 4
        1,2,3,4,5
        l r(r = n - k)
        1) l = 0, r = 1, m = 0, window_index = [m, m + k - 1] => [0, 3] val: [1,2, 3, 4]
           check right most of the window - x
           x - a[m + k]  = 3 - a[0 + 4] = 3 - 5 = -2,  m + k is the right element just outside of the window
            check x - leftmost of the window,
            i.e. if move one step to the right, will the new window closer than the old window?
            a[m] - x = 1 - 3 = -2
            x - a[m + k] == a[m] - x (if < , means new window is closer, cool, then move right, else. move left)
            move left, r = m = 0
            l == r == 0, termiate

        """
        l, r = 0, len(arr) - k
        while l < r:
            m = l + (r - l) // 2 # m is the left boudary of the window, right boundry is m + k - 1
            # nums[m + k] is the element just outside the window,
            # if nums[m + k] - x < x - nums[m], means, if just shift the window one step to the right,
            # the new window is more closer than the old window, then we need to move the window to right,
            # l = m + 1
            # otherwise, move to left, r = m
            if arr[m + k] - x < x - arr[m]:
                l = m + 1
            else:
                r = m
        return arr[l: l + k]

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # l
        # 1,1,2,3,4,5 [1, 1, 2, 3] -1
        #         r
        q = collections.deque()
        for r in range(len(arr)):
            if len(q) < k:
                q.append(arr[r])
            else:
                if arr[r] == q[0] or abs(arr[r] - x) < abs(q[0] - x):
                    q.popleft()
                    q.append(arr[r])
                else:
                    break
        return list(q)