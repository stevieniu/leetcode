"""
269. Alien Dictionary
https://leetcode.com/problems/alien-dictionary/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary. Now it is claimed that the strings in words are sorted lexicographically by the rules of this new language.

If this claim is incorrect, and the given arrangement of string in words cannot correspond to any order of letters, return "".

Otherwise, return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there are multiple solutions, return any of them.



Example 1:

Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
Example 2:

Input: words = ["z","x"]
Output: "zx"
Example 3:

Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".


Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of only lowercase English letters.
"""

from  typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        g = {c: set() for word in words for c in word}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            n = min(len(w1), len(w2))
            if w1[:n] == w2[:n] and len(w1) > len(w2): return ""
            for j in range(n):
                if w1[j] != w2[j]:
                    if w2[j] not in g[w1[j]]:
                        g[w1[j]].add(w2[j])
                    break
        UNVISITED, VISITING, VISITED = 0, 1, 2
        state = {c: UNVISITED for word in words for c in word}
        ans = []

        def dfs(node):
            if state[node] == VISITED:
                return True
            elif state[node] == VISITING:
                return False

            state[node] = VISITING

            for nei in g[node]:
                if not dfs(nei):
                    return False
            state[node] = VISITED
            ans.append(node)
            return True

        for c in g:
            if not dfs(c):
                return ''
        return ''.join(reversed(ans))
