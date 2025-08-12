"""
825. Friends Of Appropriate Ages
https://leetcode.com/problems/friends-of-appropriate-ages/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

There are n persons on a social media website. You are given an integer array ages where ages[i] is the age of the ith person.

A Person x will not send a friend request to a person y (x != y) if any of the following conditions is true:

age[y] <= 0.5 * age[x] + 7
age[y] > age[x]
age[y] > 100 && age[x] < 100
Otherwise, x will send a friend request to y.

Note that if x sends a request to y, y will not necessarily send a request to x. Also, a person will not send a friend request to themself.

Return the total number of friend requests made.



Example 1:

Input: ages = [16,16]
Output: 2
Explanation: 2 people friend request each other.
Example 2:

Input: ages = [16,17,18]
Output: 2
Explanation: Friend requests are made 17 -> 16, 18 -> 17.
Example 3:

Input: ages = [20,30,100,110,120]
Output: 3
Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.


Constraints:

n == ages.length
1 <= n <= 2 * 104
1 <= ages[i] <= 120
"""
from  typing import List
import collections

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        def can_send_request(a, b):
            if b > .5 * a + 7 and a >= b:
                return True
            return False

        counter = collections.Counter(ages)
        ans = 0
        for a, freq_a in counter.items():
            for b, freq_b in counter.items():
                if can_send_request(a, b):
                    ans += freq_a * freq_b
                    if a == b:
                        ans -= freq_a
        return ans


