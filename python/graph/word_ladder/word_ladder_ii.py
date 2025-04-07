"""
126. https://leetcode.com/problems/word-ladder-ii/description/
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].



Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.


Constraints:

1 <= beginWord.length <= 5
endWord.length == beginWord.length
1 <= wordList.length <= 500
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
The sum of all shortest transformation sequences does not exceed 105.
"""
from typing import List
import collections
import string

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        def dfs(curr_word):
            if curr_word == beginWord:
                ans.append(path[::-1])
                return
            for predessor in node_predessors[curr_word]:
                path.append(predessor)
                dfs(predessor)
                path.pop()

        dist_from_begin = {beginWord: 0}  # word: distance  from beginWord
        node_predessors = collections.defaultdict(
            set)  # direct predessors of the current node {currNode: {pred1, pred2...}}
        word_set = set(wordList)
        word_set.discard(beginWord)
        q = collections.deque([beginWord])
        if endWord not in word_set:
            return []

        found = False
        step = 0
        while q:
            step += 1
            for _ in range(len(q)):
                predssor = q.popleft()
                for i in range(len(beginWord)):
                    for c in string.ascii_lowercase:
                        new_word = predssor[:i] + c + predssor[i + 1:]
                        # preventing dropping another path
                        if dist_from_begin.get(new_word, 0) == step:
                            node_predessors[new_word].add(predssor)

                        if new_word in word_set:
                            node_predessors[new_word].add(predssor)
                            word_set.discard(new_word)
                            q.append(new_word)
                            dist_from_begin[new_word] = step
                            if new_word == endWord:
                                found = True
                print()

        ans = []
        path = [endWord]
        if found:
            dfs(endWord)
        return ans


beginWord = 'hit'
endWord = 'cog'
wordList = ["hot","dot","dog","lot","log","cog"]
Solution().findLadders(beginWord, endWord, wordList)