"""
2222. https://leetcode.com/problems/number-of-ways-to-select-buildings/description/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency

You are given a 0-indexed binary string s which represents the types of buildings along a street where:

s[i] = '0' denotes that the ith building is an office and
s[i] = '1' denotes that the ith building is a restaurant.
As a city official, you would like to select 3 buildings for random inspection. However, to ensure variety, no two consecutive buildings out of the selected buildings can be of the same type.

For example, given s = "001101", we cannot select the 1st, 3rd, and 5th buildings as that would form "011" which is not allowed due to having two consecutive buildings of the same type.
Return the number of valid ways to select 3 buildings.



Example 1:

Input: s = "001101"
Output: 6
Explanation:
The following sets of indices selected are valid:
- [0,2,4] from "001101" forms "010"
- [0,3,4] from "001101" forms "010"
- [1,2,4] from "001101" forms "010"
- [1,3,4] from "001101" forms "010"
- [2,4,5] from "001101" forms "101"
- [3,4,5] from "001101" forms "101"
No other selection is valid. Thus, there are 6 total ways.
Example 2:

Input: s = "11100"
Output: 0
Explanation: It can be shown that there are no valid selections.


Constraints:

3 <= s.length <= 105
s[i] is either '0' or '1'.
"""
class Solution:
    def numberOfWays(self, s: str) -> int:
        # 001101
        # cnt of pattern 010 * cnt of pattern 101
        # cnt of pattenr 010 = cnt of 0 on the left of the current index i * cnt of 0 on the right of i
        # cnt of pattern 101 = cnt of 1 on the left of the current index i * cnt of 1 on the right of i
        # e.g. s = 101010,
        # when i = 1, s[i] = 0, cnt of 1 of left of i = 1 is 1, cnt of 1 on the right of i = 1 is 2
        # so cnt of 101 when i == 1 is 1 * 2 = 2 => 1(i = 0)0(i=1)(1=2) and 1(i=0)0(i=1)1(i=4)
        cnt0, cnt1 = s.count('0'), s.count('1')
        left_0_so_far, left_1_so_far = 0, 0
        ans = 0
        for c in s:
            if c == '0':
                left_0_so_far += 1
                ans += left_1_so_far * (cnt1 - left_1_so_far)
            else:
                left_1_so_far += 1
                ans += left_0_so_far * (cnt0 - left_0_so_far)
        return ans