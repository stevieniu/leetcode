"""
139. Word Break
https://leetcode.com/problems/word-break/description/

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.



Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false


Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.

"""
from typing import List
from functools import lru_cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (1 + len(s))
        dp[0] = True

        for i in range(1, len(s) + 1):
            for word in wordDict:
                if s[max(0, i - len(word)): i] == word and dp[i - len(word)]:
                    dp[i] = True
                    break
        return dp[-1]

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # catsandog", wordDict = ["cats","dog","sand","and","cat"]
        @lru_cache(None)
        def dfs(i):  # can s[i:] be spearated into words in wordDict?
            if i == len(s):
                return True

            for word in wordDict:
                if s[i: i + len(word)] == word and dfs(i + len(word)):
                    return True
            return False

        return dfs(0)