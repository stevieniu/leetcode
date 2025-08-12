"""
1539. Kth Missing Positive Number
https://leetcode.com/problems/kth-missing-positive-number/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.



Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
Example 2:

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.


Constraints:

1 <= arr.length <= 1000
1 <= arr[i] <= 1000
1 <= k <= 1000
arr[i] < arr[j] for 1 <= i < j <= arr.length


Follow up:

Could you solve this problem in less than O(n) complexity?
"""

from typing import List
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # 2,3,4,7,11
        # 1,5,6,8,9,10
        data_set = set(arr)
        i = 1

        while True:
            if i not in data_set:
                k -= 1
            if k == 0:
                return i
            i += 1

    def findKthPositive(self, arr: List[int], k: int) -> int:
        for i in range(len(arr)):
            if arr[i] <= k:
                k += 1
            else:
                break
        return k

    # binary search O(log(n))
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l, r = 0, len(arr) - 1
        # number of missing numbers = arr[i] - (i + 1)
        while l <= r:
            m = (l + r) // 2
            if arr[m] - (m + 1) < k:
                l = m + 1
            else:
                r = m - 1
        # now l = r + 1, kth missing number is between arr[right] and arr[left]
        # number of missing numbers for r is arr[r] - (r + 1)
        # ans = arr[r] + more => more = k - missing number at r = k - (arr[r] - [r + 1])   =>
        #     = arr[r] + (  k - (arr[r] - (r + 1))  ) = k + r + 1 = k + l
        return k + l


arr = [2,3,4,7,11]
k = 6
print(Solution().findKthPositive(arr, k))