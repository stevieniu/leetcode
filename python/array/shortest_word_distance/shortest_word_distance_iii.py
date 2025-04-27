"""
245. Shortest Word Distance III
https://leetcode.com/problems/shortest-word-distance-iii/description/

Given an array of strings wordsDict and two strings that already exist in the array word1 and word2, return the shortest distance between the occurrence of these two words in the list.

Note that word1 and word2 may be the same. It is guaranteed that they represent two individual words in the list.



Example 1:

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
Output: 1
Example 2:

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "makes"
Output: 3


Constraints:

1 <= wordsDict.length <= 105
1 <= wordsDict[i].length <= 10
wordsDict[i] consists of lowercase English letters.
word1 and word2 are in wordsDict.
"""

from typing import List
class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        n = len(wordsDict)
        i1 = i2 = -1
        min_dist = n
        for i, word in enumerate(wordsDict):
            if word == word1:
                i1 = i
            if word == word2:
                if word2 == word1:
                    i1 = i2
                i2 = i
            if i1 != -1 and i2 != -1:
                min_dist = min(min_dist, abs(i1 - i2))
        return min_dist

    #     "a", "c", "a", "a",
    #                i
    #
    # i1 = 0, i2 = 2 min_dist
