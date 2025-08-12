"""
2982. Find Longest Special Substring That Occurs Thrice II
https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-ii/description/

You are given a string s that consists of lowercase English letters.

A string is called special if it is made up of only a single character. For example, the string "abc" is not special, whereas the strings "ddd", "zz", and "f" are special.

Return the length of the longest special substring of s which occurs at least thrice, or -1 if no special substring occurs at least thrice.

A substring is a contiguous non-empty sequence of characters within a string.



Example 1:

Input: s = "aaaa"
Output: 2
Explanation: The longest special substring which occurs thrice is "aa": substrings "aaaa", "aaaa", and "aaaa".
It can be shown that the maximum length achievable is 2.
Example 2:

Input: s = "abcdef"
Output: -1
Explanation: There exists no special substring which occurs at least thrice. Hence return -1.
Example 3:

Input: s = "abcaba"
Output: 1
Explanation: The longest special substring which occurs thrice is "a": substrings "abcaba", "abcaba", and "abcaba".
It can be shown that the maximum length achievable is 1.


Constraints:

3 <= s.length <= 5 * 105
s consists of only lowercase English letters.
"""
import collections
import string
class Solution:
    def maximumLength(self, s: str) -> int:
        #      n = 4
        #e.g. aaaa aaa  aa
        #
        # 1. group chars, {a: [4, 3, 2]} # char: [length of each group], n is the longest length among all groups, to occur 3 times, n -2 always work
        # 2. if there are 2 groups, if the second group is one less shorter than the first group length, the second group length is the longest substring length
        # 3. if there are 3 groups, if the 3 string are equal length, the longest substring is the n
        #
        #
        groups = collections.defaultdict(list) # char: [length of groups]
        for i, c in enumerate(s):
            if i == 0 or c != s[i - 1]:
                groups[c].append(1)
            else:
                groups[c][-1] += 1
        for k in groups:
            groups[k].sort(reverse=True)
            groups[k] = groups[k][:3]
        print(groups)
        res = -1
        for c in string.ascii_lowercase:
            if c not in groups:
                continue
            print(c)
            grps = groups[c] # [1, 2, 3]
            grp_size = len(grps)
            # case 1: only 1 group of c, longest len is n - 2
            ans = grps[0] - 2
            # case2: 2 groups of c, if second group lenth is n - 1, then longest len is n - 1
            if grp_size == 2:
                # aa a
                x, y = grps # x is the length of first group, y is the length of 2nd group
                if x <= y + 1:
                    ans = max(ans, x - 1)
            # case 3: 3 groups, if second group lenth is n - 1, then longest len is n - 1
            # if 3rd group len is n - 2, longest len is n - 2
            elif grp_size == 3:
                x, y , z = grps
                if x == y == z:
                    ans = max(ans, x)
                elif x <= y + 1:
                    ans = max(ans, x - 1)
            if ans > 0:
                res = max(res, ans)
        return res