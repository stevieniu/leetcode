"""
670. Maximum Swap
https://leetcode.com/problems/maximum-swap/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.



Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.


Constraints:

0 <= num <= 108
"""

import collections
class Solution:
    def maximumSwap(self, num: int) -> int:
        if num <= 11:
            return num
        # 8 3 7 6
        # starting from highest digit, looking for the biggest number on the right of current number, and do swap
        q = collections.deque()
        while num:
            q.appendleft(num % 10)
            num //= 10

        max_seen, max_seen_at = -1, len(q)
        i = len(q) - 1
        while i >= 0:
            curr = q[i]
            q[i] = (curr, max_seen, max_seen_at)
            if curr > max_seen:
                max_seen = curr
                max_seen_at = i
            i -= 1

        i = 0
        while i < len(q):
            curr, max_seen, max_seen_at = q[i]
            if max_seen > curr:
                q[i], q[max_seen_at] = q[max_seen_at], q[i]
                break
            i += 1
        ans = 0
        for curr, _, _ in q:
            ans = 10 * ans + curr
        return ans
