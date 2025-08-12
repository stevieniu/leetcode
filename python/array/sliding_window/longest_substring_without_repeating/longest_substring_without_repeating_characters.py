"""
3. https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

Given a string s, find the length of the longest substring without duplicate characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #  l
        # aa {  }  maxx = 3
        #  r
        data_set = set()
        l = 0
        maxx = 0
        for r in range(len(s)):
            while l < r and s[r] in data_set:
                data_set.remove(s[l])
                l += 1
            data_set.add(s[r])
            maxx = max(maxx, len(data_set))
        return maxx
