"""
1711. Count Good Meals
https://leetcode.com/problems/count-good-meals/description/

A good meal is a meal that contains exactly two different food items with a sum of deliciousness equal to a power of two.

You can pick any two different foods to make a good meal.

Given an array of integers deliciousness where deliciousness[i] is the deliciousness of the i​​​​​​th​​​​​​​​ item of food, return the number of different good meals you can make from this list modulo 109 + 7.

Note that items with different indices are considered different even if they have the same deliciousness value.



Example 1:

Input: deliciousness = [1,3,5,7,9]
Output: 4
Explanation: The good meals are (1,3), (1,7), (3,5) and, (7,9).
Their respective sums are 4, 8, 8, and 16, all of which are powers of 2.
Example 2:

Input: deliciousness = [1,1,1,3,3,3,7]
Output: 15
Explanation: The good meals are (1,1) with 3 ways, (1,3) with 9 ways, and (1,7) with 3 ways.


Constraints:

1 <= deliciousness.length <= 105
0 <= deliciousness[i] <= 220
"""

from typing import List
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        cnt = 0
        cache = {}
        # 2^20 + 2^20 = 2^21, so the biggest possible number is 2^21
        # 2^0 == 1<<0, 2^1 == 1<<1, ... 2^8 ==1<<8, ... 2^21 == 1<<21
        for n in deliciousness:
            for i in range(22):
                target = (1 << i) - n  # power of 2 => 1 << 0, 1 << 1, 1 << 2, ... 1 << 21
                if target in cache:
                    cnt += cache[target]
            cache[n] = cache.get(n, 0) + 1
        return cnt % (10 ** 9 + 7)

        # 1 1 1 1
        #       i
        # target = 2 {1: 4}
        # cnt = 6