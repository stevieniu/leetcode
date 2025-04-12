"""
76. Minimum Window Substring

Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.



Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.


Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.


Follow up: Could you find an algorithm that runs in O(m + n) time?
"""

import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0 or len(s) < len(t):
            return ""
        counter = collections.Counter(t)
        window = collections.defaultdict(int)

        have, need = 0, len(counter)
        res_idx = [-1, -1]
        l = 0
        min_size = float('inf')
        for r in range(len(s)):
            window[s[r]] += 1
            if s[r] in counter and window[s[r]] == counter[s[r]]:  # mean already have all s[r]
                have += 1
            while have == need:  # means s[l: r] contains all characters in t
                if min_size > r - l + 1:
                    min_size = r - l + 1
                    res_idx = [l, r]

                window[s[l]] -= 1
                if s[l] in counter and window[s[l]] < counter[s[l]]:
                    have -= 1
                l += 1
        return s[res_idx[0]: res_idx[1] + 1]

    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t): return ''

        #               r
        # s = "ADOBECODEBANC", t = "ABC"  {A: 0, B: 0, C: 1},   count = 1
        #       l
        #  minn = 6
        counter = collections.Counter(t)  # whenever counter[key] == 0, count should descrease by 1
        count = len(counter)  # if count descrese to 0, found a valid substring
        min_len = float('inf')
        ans = [-1, -1]  # index of substring
        l = 0
        for r in range(len(s)):
            if s[r] not in counter: continue
            counter[s[r]] -= 1
            if counter[s[r]] == 0:
                count -= 1
            while count == 0:
                if min_len > r - l + 1:
                    min_len = r - l + 1
                    ans[0], ans[1] = l, r
                if s[l] in counter:
                    counter[s[l]] += 1
                    if counter[s[l]] > 0:
                        count += 1
                l += 1
        return s[ans[0]: ans[1] + 1] if min_len != float('inf') else ''
