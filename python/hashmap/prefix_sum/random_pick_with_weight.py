"""
528. Random Pick with Weight
https://leetcode.com/problems/random-pick-with-weight/description/

You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.

You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).

For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).


Example 1:

Input
["Solution","pickIndex"]
[[[1]],[]]
Output
[null,0]

Explanation
Solution solution = new Solution([1]);
solution.pickIndex(); // return 0. The only option is to return 0 since there is only one element in w.
Example 2:

Input
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output
[null,1,1,1,1,0]

Explanation
Solution solution = new Solution([1, 3]);
solution.pickIndex(); // return 1. It is returning the second element (index = 1) that has a probability of 3/4.
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 0. It is returning the first element (index = 0) that has a probability of 1/4.

Since this is a randomization problem, multiple answers are allowed.
All of the following outputs can be considered correct:
[null,1,1,1,1,0]
[null,1,1,1,1,1]
[null,1,1,1,0,0]
[null,1,1,1,0,1]
[null,1,0,1,0,0]
......
and so on.


Constraints:

1 <= w.length <= 104
1 <= w[i] <= 105
pickIndex will be called at most 104 times.
"""
from typing import List
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

    # O(n)
    def pickIndex(self) -> int:
        ran = random.randint(1, self.total)
        for i, weight in enumerate(self.w):
            if ran <= weight:
                return i
    # O(log(N))
    def pickIndex(self) -> int:
        ran = random.randint(1, self.total)
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