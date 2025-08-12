"""
2067. Number of Equal Count Substrings
https://leetcode.com/problems/number-of-equal-count-substrings/description/

You are given a 0-indexed string s consisting of only lowercase English letters, and an integer count. A substring of s is said to be an equal count substring if, for each unique letter in the substring, it appears exactly count times in the substring.

Return the number of equal count substrings in s.

A substring is a contiguous non-empty sequence of characters within a string.



Example 1:

Input: s = "aaabcbbcc", count = 3
Output: 3
Explanation:
The substring that starts at index 0 and ends at index 2 is "aaa".
The letter 'a' in the substring appears exactly 3 times.
The substring that starts at index 3 and ends at index 8 is "bcbbcc".
The letters 'b' and 'c' in the substring appear exactly 3 times.
The substring that starts at index 0 and ends at index 8 is "aaabcbbcc".
The letters 'a', 'b', and 'c' in the substring appear exactly 3 times.
Example 2:

Input: s = "abcd", count = 2
Output: 0
Explanation:
The number of times each letter appears in s is less than count.
Therefore, no substrings in s are equal count substrings, so return 0.
Example 3:

Input: s = "a", count = 5
Output: 0
Explanation:
The number of times each letter appears in s is less than count.
Therefore, no substrings in s are equal count substrings, so return 0


Constraints:

1 <= s.length <= 3 * 104
1 <= count <= 3 * 104
s consists only of lowercase English letters.
"""
from collections import Counter
import collections
class Solution:
    def equalCountSubstrings(self, s: str, count: int) -> int:
        # fixed window . window size must be mutiples of count, i.e. count x [1 ~ 26]
        # try every window from size count to size 26 x count
        # time complexity is O(N) * 26
        cnt, n = 0, len(s)
        for i in range(1, 27):
            L = i * count
            if L > n: break
            l, d = 0, Counter()
            for r, c in enumerate(s):
                d[c] += 1
                if r - l + 1 == L:
                    if all(x == count or x == 0 for x in d.values()):
                        cnt += 1
                    d[s[l]] -= 1
                    l += 1

        return cnt

    def equalCountSubstrings(self, s: str, count: int) -> int:
        ans, N = 0, len(s)
        for i in range(1, 27):
            L = count * i
            if L > N: break
            l, counter = 0, collections.defaultdict(int)
            for r, c in enumerate(s):
                counter[c] += 1
                if r - l + 1 == L:
                    flag = True
                    for k in counter:
                        if counter[k] != count:
                            print(counter[k])
                            flag = False
                            break
                    if flag:
                        ans += 1
                    counter[s[l]] -= 1
                    if counter[s[l]] == 0:
                        del counter[s[l]]
                    l += 1
        return ans