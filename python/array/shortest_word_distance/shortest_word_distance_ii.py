"""
244. Shortest Word Distance II
https://leetcode.com/problems/shortest-word-distance-ii/description/?envType=company&envId=linkedin&favoriteSlug=linkedin-thirty-days

Design a data structure that will be initialized with a string array, and then it should answer queries of the shortest distance between two different strings from the array.

Implement the WordDistance class:

WordDistance(String[] wordsDict) initializes the object with the strings array wordsDict.
int shortest(String word1, String word2) returns the shortest distance between word1 and word2 in the array wordsDict.


Example 1:

Input
["WordDistance", "shortest", "shortest"]
[[["practice", "makes", "perfect", "coding", "makes"]], ["coding", "practice"], ["makes", "coding"]]
Output
[null, 3, 1]

Explanation
WordDistance wordDistance = new WordDistance(["practice", "makes", "perfect", "coding", "makes"]);
wordDistance.shortest("coding", "practice"); // return 3
wordDistance.shortest("makes", "coding");    // return 1


Constraints:

1 <= wordsDict.length <= 3 * 104
1 <= wordsDict[i].length <= 10
wordsDict[i] consists of lowercase English letters.
word1 and word2 are in wordsDict.
word1 != word2
At most 5000 calls will be made to shortest.
"""
import collections
from typing import List
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.wordsDict = wordsDict
        self.cache = collections.defaultdict(list) # word1:[i1,i2,....], word2: [j1,j2,...]
        for i, word in enumerate(wordsDict):
            self.cache[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        id1_lst = self.cache[word1]
        id2_lst = self.cache[word2]
        n = len(self.wordsDict)
        min_dist = n
        i1 = i2 = 0
        while i1 < len(id1_lst) and i2 < len(id2_lst):
            min_dist = min(min_dist, abs(id1_lst[i1] - id2_lst[i2]))
            if id1_lst[i1] < id2_lst[i2]:
                i1 += 1
            else:
                i2 += 1
        return min_dist




# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)