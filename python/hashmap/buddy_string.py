"""
859. https://leetcode.com/problems/buddy-strings/?envType=study-plan-v2&envId=programming-skills

Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

For example, swapping at indices 0 and 2 in "abcd" results in "cbad".


Example 1:

Input: s = "ab", goal = "ba"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.
Example 2:

Input: s = "ab", goal = "ab"
Output: false
Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.
Example 3:

Input: s = "aa", goal = "aa"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.


Constraints:

1 <= s.length, goal.length <= 2 * 104
s and goal consist of lowercase letters.

"""
from collections import Counter
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        c1, c2 = Counter(s), Counter(goal)
        if c1 != c2: return False
        diff_cnt = 0
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff_cnt += 1
                if diff_cnt > 2:
                    return False
        if diff_cnt == 2:
            return True
        else:
            # s and goal are equal, in this case, if there are two indices (i, j) can be swaped,
            # s[i] == s[j]
            for key in c1:
                if c1[key] > 1:
                    return True
            return False

