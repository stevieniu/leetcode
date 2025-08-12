"""
159. Longest Substring with At Most Two Distinct Characters
https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/description/

Given a string s, return the length of the longest substring that contains at most two distinct characters.



Example 1:

Input: s = "eceba"
Output: 3
Explanation: The substring is "ece" which its length is 3.
Example 2:

Input: s = "ccaabbb"
Output: 5
Explanation: The substring is "aabbb" which its length is 5.


Constraints:

1 <= s.length <= 105
s consists of English letters.
"""

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        #       r
        # ccaabbb
        # l
        #
        # {, a: 1, b:2} ans = 5
        word_counter = {}
        ans = 0
        l = 0
        for r in range(len(s)):
            while len(word_counter) == 2 and s[r] not in word_counter:
                word_counter[s[l]] -= 1
                if word_counter[s[l]] == 0:
                    del word_counter[s[l]]
                l += 1
            word_counter[s[r]] = word_counter.get(s[r], 0) + 1
            ans = max(ans, r - l + 1)
        return ans
