"""
68. Text Justification
https://leetcode.com/problems/text-justification/description/

Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.


Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.
Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]


Constraints:

1 <= words.length <= 300
1 <= words[i].length <= 20
words[i] consists of only English letters and symbols.
1 <= maxWidth <= 100
words[i].length <= maxWidth
"""
from typing import List
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        line = []
        len_of_line = 0 # length of total words, not include space

        i = 0
        while i < len(words):
            if len(line) + len_of_line + len(words[i]) > maxWidth:
                # add line to ans
                spaces = (maxWidth - len_of_line) // max(1, len(line) - 1) # spaces number following each word
                space_remainder =  (maxWidth - len_of_line) % max(1, len(line) - 1)# after evenly allocate spaces, how many spaces left

                # append spaces to each word in the line
                for j in range(max(1, len(line) - 1)):
                    line[j] += ' ' * spaces
                    if space_remainder > 0:
                        line[j] += ' '
                        space_remainder -= 1
                ans.append(''.join(line))
                # reset line
                line = []
                len_of_line = 0
            line.append(words[i])
            len_of_line += len(words[i])
            i += 1


        # last line
        print(ans)
        last_line = ' '.join(line)
        spaces = maxWidth - len(last_line)
        ans.append(last_line + ' ' * spaces)
        return ans