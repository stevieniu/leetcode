"""
2260. Minimum Consecutive Cards to Pick Up
https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/description/

You are given an integer array cards where cards[i] represents the value of the ith card. A pair of cards are matching if the cards have the same value.

Return the minimum number of consecutive cards you have to pick up to have a pair of matching cards among the picked cards. If it is impossible to have matching cards, return -1.



Example 1:

Input: cards = [3,4,2,3,4,7]
Output: 4
Explanation: We can pick up the cards [3,4,2,3] which contain a matching pair of cards with value 3. Note that picking up the cards [4,2,3,4] is also optimal.
Example 2:

Input: cards = [1,0,5,3]
Output: -1
Explanation: There is no way to pick up a set of consecutive cards that contain a pair of matching cards.


Constraints:

1 <= cards.length <= 105
0 <= cards[i] <= 106




exactly the same with 3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
"""
from typing import List
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        #       r
        # 3,4,2,4,3,7
        #   l
        # {3, 4,2, }
        # ans = 3
        card_set = set()
        ans = float('inf')
        l = 0
        for r in range(len(cards)):
            while cards[r] in card_set:
                ans = min(ans, r - l + 1)
                card_set.remove(cards[l])
                l += 1
            card_set.add(cards[r])

        return ans if ans != float('inf') else -1