"""
556. Next Greater Element III
https://leetcode.com/problems/next-greater-element-iii/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.



Example 1:

Input: n = 12
Output: 21
Example 2:

Input: n = 21
Output: -1


Constraints:

1 <= n <= 231 - 1
"""
import collections

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        MAX = 2 ** 31 - 1
        #  123
        arr = collections.deque([])
        while n:
            val = n % 10
            arr.appendleft(val)
            n //= 10
        arr = list(arr)
        pivot = 0  # arr[pivot:] is in descreasing order
        for i in range(len(arr) - 1, 0, -1):
            if arr[i - 1] < arr[i]:
                pivot = i
                break
        if pivot == 0:
            return -1

        # from right of arr, looking for the first number > arr[pivot]
        for i in range(len(arr) - 1, pivot - 1, -1):
            if arr[i] > arr[pivot - 1]:
                arr[i], arr[pivot - 1] = arr[pivot - 1], arr[i]
                break

        # 12543
        # 13542
        arr[pivot:] = sorted(arr[pivot:])
        ans = 0
        for n in arr:
            if ans > MAX // 10 or ans == MAX // 10 and n >= 8:
                return -1
            ans = 10 * ans + n

        return ans