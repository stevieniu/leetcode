"""
44. Wildcard Matching
https://leetcode.com/problems/wildcard-matching/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).



Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.


Constraints:

0 <= s.length, p.length <= 2000
s contains only lowercase English letters.
p contains only lowercase English letters, '?' or '*'.
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pp = sp = 0
        star = -1  # index of star in p
        match_star_idx = 0  # index to match * in s
        while sp < len(s):
            if pp < len(p) and (s[sp] == p[pp] or p[pp] == '?'):
                sp += 1
                pp += 1
            elif pp < len(p) and p[pp] == '*':  # * to match s[sp] or match empty string
                star = pp  # star is the index of *, pp move to next char
                pp += 1
                # don't move sp, because * can match empty string
                match_star_idx = sp
            elif star != -1:  # previous p[pp] is *, starting to match *
                match_star_idx += 1 # this is to reset sp and pp, consider case: p = "abcabczzzde", s = "*abc???de*"
                sp = match_star_idx
                pp = star + 1  # pp point to the index right after *
            else:
                # reach the end of p but have' reach the end of s
                return False
                #             star
                # s = caa p = *    d
                #                 pp
                #
        while pp < len(p) and p[pp] == '*':
            pp += 1
        return pp == len(p)


s = 'cacd'
p = '*ca'
Solution().isMatch(s, p)



