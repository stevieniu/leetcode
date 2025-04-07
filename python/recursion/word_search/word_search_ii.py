"""
212. https://leetcode.com/problems/word-search-ii/description/

Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.



Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []


Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
"""
from typing import List

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if curr.children[idx] is None:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.is_word = True

    def search(self, word):
        curr = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if curr.children[idx] is None: return None
            curr = curr.children[idx]
        return curr if curr.is_word else None

    def delete(self, word):
        node = self.search(word)
        if node is not None:
            node.is_word = False


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROW, COL = len(board), len(board[0])
        visit = set()

        def dfs(s, trie_node, i, j):
            if i < 0 or i == ROW or j < 0 or j == COL or (i, j) in visit or \
                    trie_node.children[ord(board[i][j]) - ord('a')] is None:
                return

            s += board[i][j]
            trie_node = trie_node.children[ord(board[i][j]) - ord('a')]
            if trie_node.is_word:
                ans.append(s)
                trie.delete(s)

            visit.add((i, j))
            for dr, dc in DIRECTIONS:
                nxt_i, nxt_j = i + dr, j + dc
                dfs(s, trie_node, nxt_i, nxt_j)
            visit.remove((i, j))

        ans = []
        for i in range(ROW):
            for j in range(COL):
                dfs('', trie.root, i, j)
        return ans