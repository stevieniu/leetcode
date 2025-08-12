"""
480. Sliding Window Median
https://leetcode.com/problems/sliding-window-median/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.

For examples, if arr = [2,3,4], the median is 3.
For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.
You are given an integer array nums and an integer k. There is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the median array for each window in the original array. Answers within 10-5 of the actual value will be accepted.



Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
Explanation:
Window position                Median
---------------                -----
[1  3  -1] -3  5  3  6  7        1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7        3
 1  3  -1  -3 [5  3  6] 7        5
 1  3  -1  -3  5 [3  6  7]       6
Example 2:

Input: nums = [1,2,3,4,2,3,1,4,2], k = 3
Output: [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]


Constraints:

1 <= k <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
"""
import heapq
from typing import List
import collections
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # 1,3,-1,-3,5,3,6,7
        #         i
        # [ 1, 3, -1, -3]
        # [1, -1, -3, 3, 5, 6]
        max_heap = []  # store numbers <= median ,i.e. in the sorted array, store the  left part of the middle point.   max_heap will be 1 more number than min_heap or equal to min_heap
        min_heap = []  # store numbers > median, i.e.  n the sorted array, store the  right part of the middle point
        # len(max_heap) == len(min_heap) or len(max_heap) == len(min_heap)+ 1

        ans = []
        for i in range(k):
            heapq.heappush(max_heap, -nums[i])
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
            if len(min_heap) > len(max_heap):
                heapq.heappush(max_heap, -heapq.heappop(min_heap))

        median = (-max_heap[0] + min_heap[0]) / 2 if k % 2 == 0 else -max_heap[0]
        ans.append(median)

        number_to_pop = collections.defaultdict(int)  # {numbet to be poped: cnt} if cnt > 0, need pop

        for i in range(k, len(nums)):
            prev = nums[i - k]  # number to be popped
            number_to_pop[prev] += 1

            # balance == 0 means the number of elements in both min_heap and max_heap are balanced, ready to calculate median
            # blance = 1 means 1 more elements in max_heap, need to pop from max_heap and add to min_heap
            # blance = -1 means 1 more elements in min_heap, need to pop from min_heao and add to max_heap

            # if prev <= meidan, means prev is in max_heap, once poped, max_heap is one element less, balance == -1
            # if prev > median, means prev is in min_heap, once popped, min_heap is one element less
            balance = -1 if prev <= median else 1
            if nums[i] <= median:  # nums[i] need to add to max_heap, balance += 1
                balance += 1
                heapq.heappush(max_heap, -nums[i])
            else:  # nums[i] need to add to min_heap, balance -= 1
                balance -= 1
                heapq.heappush(min_heap, nums[i])

            if balance > 0:  # more elements in max_heap, need to pop from max_heap and insert to min_heap
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
            elif balance < 0:
                heapq.heappush(max_heap, -heapq.heappop(min_heap))

            while max_heap and number_to_pop[-max_heap[0]] > 0:
                number_to_pop[-max_heap[0]] -= 1
                heapq.heappop(max_heap)
            while min_heap and number_to_pop[min_heap[0]] > 0:
                number_to_pop[min_heap[0]] -= 1
                heapq.heappop(min_heap)

            median = (-max_heap[0] + min_heap[0]) / 2 if k % 2 == 0 else -max_heap[0]
            ans.append(median)

        return ans


nums = [1, 2, 3, 4]
k = 3
Solution().medianSlidingWindow(nums, k)
