"""
253. Meeting Rooms II
https://leetcode.com/problems/meeting-rooms-ii/description/

Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.



Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1


Constraints:

1 <= intervals.length <= 104
0 <= starti < endi <= 106
"""

from typing import List
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        rooms = []  # store meeting ending time, the earliest ending time is on the top
        heapq.heappush(rooms, intervals[0][1])

        for s, e in intervals[1:]:
            if s >= rooms[0]:  # in this case, the next starting time is later than the earliest ending time, can reuse this ealiest ending meeting room
                heapq.heappop(rooms)
            heapq.heappush(rooms, e)
        return len(rooms)
