"""
38. Count and Say
https://leetcode.com/problems/count-and-say/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the run-length encoding of countAndSay(n - 1).
Run-length encoding (RLE) is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "3322251" we replace "33" with "23", replace "222" with "32", replace "5" with "15" and replace "1" with "11". Thus the compressed string becomes "23321511".

Given a positive integer n, return the nth element of the count-and-say sequence.



Example 1:

Input: n = 4

Output: "1211"

Explanation:

countAndSay(1) = "1"
countAndSay(2) = RLE of "1" = "11"
countAndSay(3) = RLE of "11" = "21"
countAndSay(4) = RLE of "21" = "1211"
Example 2:

Input: n = 1

Output: "1"

Explanation:

This is the base case.



Constraints:

1 <= n <= 30


Follow up: Could you solve it iteratively?
"""
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return str(1)
        s = self.countAndSay(n - 1)
        s += " "
        counter = collections.defaultdict(int);
        res = []
        counter[s[0]] += 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                counter[s[i - 1]] += 1
            else:
                counter[s[i]] += 1
                res.append(str(counter[s[i - 1]]))
                res.append(s[i - 1])
                del counter[s[i - 1]]
        return ''.join(res)

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        # n = 4
        s = self.countAndSay(n - 1)
        ans = []
        # 22333
        #      i
        # 23
        i = 0
        while i < len(s):
            repeat_cnt = 1
            while i < len(s) - 1 and s[i] == s[i + 1]:
                repeat_cnt += 1
                i += 1
            num = s[i]
            ans.append(str(repeat_cnt))
            ans.append(num)
            i += 1
        return ''.join(ans)

    # iterative
    def countAndSay(self, n: int) -> str:
        stack = []
        for i in range(1, n + 1):
            if i == 1:
                stack.append('1')
            else:
                s = stack.pop()
                i = 0
                lvl = []
                while i < len(s):
                    repeat_cnt = 1
                    while i < len(s) - 1 and s[i] == s[i + 1]:
                        repeat_cnt += 1
                        i += 1
                    num = s[i]
                    lvl.append(str(repeat_cnt))
                    lvl.append(num)
                    i += 1
                stack.append(''.join(lvl))
        return stack[-1]