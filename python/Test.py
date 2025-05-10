from typing import List
import  collections
import string
from typing import Optional

from math import sqrt
import random
class Solution:

    def __init__(self, w: List[int]):
        # w = [1, 3, 4] => [1, 4, 8]  random number between[0, 8]
        # say rand = 6, it falls into [4 + 1, 8]. return index 2
        # if rand = 2, it falls into [1 + 1, 3], return index 1
        self.w = []
        total = 0
        for num in w:
            total  += num
            self.w.append(total)
        self.total = total

    def pickIndex(self) -> int:
        # ran = random.randint(1, self.total)
        ran = 6
        l, r = 0, len(self.w)
        #       r
        # 1, 4, 8
        #       l
        #    m
        # m = (0 + 2) / 2 = 1
        # ran = 7
        while l < r:
            m = (l + r) // 2
            if self.w[m] < ran:
                l += 1
            else:
                r = m
        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
s = Solution([1, 3, 6])
s.pickIndex()