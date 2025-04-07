"""
937. https://leetcode.com/problems/reorder-data-in-log-files/description/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency

You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

There are two types of logs:

Letter-logs: All words (except the identifier) consist of lowercase English letters.
Digit-logs: All words (except the identifier) consist of digits.
Reorder these logs so that:

The letter-logs come before all digit-logs.
The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
The digit-logs maintain their relative ordering.
Return the final order of the logs.



Example 1:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
Explanation:
The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".
Example 2:

Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]


Constraints:

1 <= logs.length <= 100
3 <= logs[i].length <= 100
All the tokens of logs[i] are separated by a single space.
logs[i] is guaranteed to have an identifier and at least one word after the identifier.
"""

from typing import List
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # "dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"
        # artcan, ownkitdig, artzero
        letter_logs = []
        digit_logs = []
        for log in logs:
            if log.split()[1][0].isalpha():
                letter_logs.append(log)
            else:
                digit_logs.append(log)

        ans = []
        letter_logs.sort(key=lambda x: (x.split(' ', 1)[1], x.split()[0]))
        # x.split(' ', 1)[1] means split the first word with the rest of the word
        # e.g. "let1 art can" => ["let1"], ["art can"]
        ans.extend(letter_logs)

        ans.extend(digit_logs)
        return ans

