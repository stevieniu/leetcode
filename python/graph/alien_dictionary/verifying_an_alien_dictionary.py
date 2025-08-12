"""
953. Verifying an Alien Dictionary
https://leetcode.com/problems/verifying-an-alien-dictionary/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.



Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).


Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
"""
from typing import List
import collections

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        letter_to_idx = collections.defaultdict(int)  # letter: idx
        for i, c in enumerate(order):
            letter_to_idx[c] = i

        for i in range(1, len(words)):
            w1, w2 = words[i - 1], words[i]
            n = min(len(w1), len(w2))
            if w1[: n] == w2[: n] and len(w1) > len(w2): return False
            for j in range(n):
                c1, c2 = w1[j], w2[j]
                if c1 == c2:
                    continue
                elif letter_to_idx[c1] < letter_to_idx[c2]:
                    break  # no need to compare follow chars, just to skip to compare next pair of words
                else:
                    return False
        return True


