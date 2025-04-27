"""
1089. Duplicate Zeros

https://leetcode.com/problems/duplicate-zeros/description/

Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.



Example 1:

Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:

Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]


Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 9
"""
from typing import List
import collections

class Solution:
    # one pass
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        q = collections.deque()
        for i, num in enumerate(arr):
            q.append(num)
            # if num == 0, append one more 0 to the queue
            if num == 0:
                q.append(num)
            arr[i] = q.popleft()


    # Constant space
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        duplicates = 0
        total_len = 0
        edge_case_0 = False  #if True, then 0 is the last element, can't increase one more 0
        n = len(arr)
        for i, num in enumerate(arr):
            if total_len == n:
                break
            total_len += 1
            if num == 0 and total_len < n:
                total_len += 1
                duplicates += 1
            elif num == 0 and total_len == n:
                edge_case_0 = True

        w = n - 1
        for i in range(n - 1 - duplicates, -1, -1):
            arr[w] = arr[i]
            w -= 1
            if arr[i] == 0 and edge_case_0 == True:
                edge_case_0 = False
                continue
            if arr[i] == 0 and edge_case_0 == False:
                arr[w] = arr[i]
                w -= 1