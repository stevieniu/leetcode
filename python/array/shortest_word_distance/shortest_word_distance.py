"""
243. Shortest Word Distance
https://leetcode.com/problems/shortest-word-distance/description/

Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.



Example 1:

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
Output: 3
Example 2:

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
Output: 1


Constraints:

2 <= wordsDict.length <= 3 * 104
1 <= wordsDict[i].length <= 10
wordsDict[i] consists of lowercase English letters.
word1 and word2 are in wordsDict.
word1 != word2
"""
from typing import List
class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        #                                     j
        # "practice", "makes", "perfect", "coding", "makes" | word1 = "makes", word2 = "coding"
        #                                             i
        # 2
        i = j = 0
        n = len(wordsDict)
        min_dist = n
        while i < n:
            if wordsDict[i] == word1 or wordsDict[
                i] == word2:  # when i find one of the word, j starts to look for the second word
                for j in range(i + 1, n):
                    if wordsDict[j] == wordsDict[
                        i]:  # before j finding the second word, j find the first word, means starting from this first word, the distance between first and second word, must be shorter, so just assign j to i, means i points to the more optimal first word
                        i = j
                        continue
                    elif wordsDict[j] == word1 or wordsDict[
                        j] == word2:  # j find the second word, calcuate distance, after that, move i to this word, j starts to looking for another word
                        min_dist = min(min_dist, j - i)
                        i = j
            i += 1
        return min_dist

    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        i1, i2 = -1, -1  # i1 points to word1, i2 points to word2
        min_dist = len(wordsDict)
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                i1 = i
            elif wordsDict[i] == word2:
                i2 = i
            if i1 != -1 and i2 != -1:
                min_dist = min(min_dist, abs(i1 - i2))
        return min_dist