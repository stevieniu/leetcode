"""
1094. Car Pooling
https://leetcode.com/problems/car-pooling/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.

Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.



Example 1:

Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
Example 2:

Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true


Constraints:

1 <= trips.length <= 1000
trips[i].length == 3
1 <= numPassengersi <= 100
0 <= fromi < toi <= 1000
1 <= capacity <= 105
"""
from typing import List
import heapq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # [8,2,3],[4,1,3],[1,3,6],[8,4,6],[4,4,8] 12
        #              i
        # [[4,1,3], [8,2,3], [1,3,6], [8,4,6], [4,4,8]]
        #. [(5, 2)]
        #     ---
        #  cur= 2
        # minHeap = [(5,2), (7, 3)]
        #             i
        # curP = 2 + 3
        trips.sort(key=lambda arr : arr[1]) # sorted by the second number in the array
        min_heap = [] # (end position, numPassnager)
        cur_passengers = 0
        for t in trips:
            numPassenager, start, end = t
            while min_heap and min_heap[0][0] <= start: # no drop yet
                cur_passengers -= min_heap[0][1]
                heapq.heappop(min_heap)
            cur_passengers += numPassenager
            if cur_passengers > capacity:
                return False
            heapq.heappush(min_heap, (end, numPassenager))
        return True

    #