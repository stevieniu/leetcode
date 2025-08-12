"""
383. Ransom Note
https://leetcode.com/problems/ransom-note/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.



Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true


Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter_r = Counter(ransomNote)
        counter_m = Counter(magazine)
        for key in counter_r:
            if key not in counter_m or counter_r[key] > counter_m[key]:
                return False
        return True