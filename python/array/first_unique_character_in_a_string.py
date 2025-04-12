"""
387. First Unique Character in a String

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.



Example 1:

Input: s = "leetcode"

Output: 0

Explanation:

The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:

Input: s = "loveleetcode"

Output: 2

Example 3:

Input: s = "aabb"

Output: -1



Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.

"""

import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        leetcode

        {l: 1, e: 2, t: 1, c: 1, o: 1, d: 1, e: 1}

        """
        counter = collections.Counter(s)
        for i, c in enumerate(s):
            if counter[c] == 1:
                return i
        return -1