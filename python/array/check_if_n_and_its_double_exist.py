"""
1346. Check If N and Its Double Exist
https://leetcode.com/problems/check-if-n-and-its-double-exist/description/

Given an array arr of integers, check if there exist two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]


Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
Example 2:

Input: arr = [3,1,7,11]
Output: false
Explanation: There is no i and j that satisfy the conditions.


Constraints:

2 <= arr.length <= 500
-103 <= arr[i] <= 103
"""
from typing import List
import collections

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        look_up = collections.defaultdict(int)
        for num in arr:
            look_up[num] += 1
        for num in arr:
            if num != 0 and 2 * num in look_up:
                return True

            if num == 0 and look_up[num] > 1:  # check cases like [0, 0]
                return True

        return False

    def checkIfExist(self, arr: List[int]) -> bool:
        mapping = set()  # {value: index}

        for i, num in enumerate(arr):
            if 2 * num in mapping or (num % 2 == 0 and num // 2 in mapping):
                return True
            mapping.add(num)
        return False