"""
340. Longest Substring with At Most K Distinct Characters
https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/description/

Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.



Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.


Constraints:

1 <= s.length <= 5 * 104
0 <= k <= 50
"""

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0: return 0
        word_counter = {}
        ans = 0
        l = 0
        for r in range(len(s)):
            while len(word_counter) == k and s[r] not in word_counter:
                word_counter[s[l]] -= 1
                if word_counter[s[l]] == 0:
                    del word_counter[s[l]]
                l += 1
            word_counter[s[r]] = word_counter.get(s[r], 0) + 1
            ans = max(ans, r - l + 1)
        return ans