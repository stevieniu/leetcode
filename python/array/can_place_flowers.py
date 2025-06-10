"""
605. Can Place Flowers
https://leetcode.com/problems/can-place-flowers/description/

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.



Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false


Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""

from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        while i < len(flowerbed) and n:
            if flowerbed[i] == 0:
                # 1) 00   2) 000  3) 100
                #   i        i        i
                if (i == 0 or flowerbed[i - 1] == 0) and \
                        (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                    n -= 1
                    i += 2
                else:
                    # 100
                    #  i  => current i is not valid, move to next plot
                    i += 1

            else:  # flowerbed[i] is 1, need to skip next plot
                i += 2

        return n == 0

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if n == 0: return True
        for i in range(len(flowerbed)):
            # 0, 0 or 0
            if flowerbed[i] == 1: continue
            if i == 0:
                if flowerbed[i] == 0 and (i + 1 == len(flowerbed) or flowerbed[i + 1] == 0):
                    n -= 1
                    flowerbed[i] = 1
                    if n == 0: break
            else:
                # ... 0, 0, 0,... or ... 0, 0
                if flowerbed[i - 1] == 0 and (i + 1 == len(flowerbed) or flowerbed[i + 1] == 0):
                    n -= 1
                    flowerbed[i] = 1
                    if n == 0: break
        print(n)
        return n == 0