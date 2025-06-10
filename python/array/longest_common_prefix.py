"""
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
"""
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # "flower","flow","flight"
        #    i

        # ans =2
        ans = ''
        for i in range(len(strs[0])):
            c = strs[0][i]
            for s in strs[1:]:
                if i == len(s) or s[i] != c:
                    return ans
            ans += c
        return ans