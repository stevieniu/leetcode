"""
621. Task Scheduler
https://leetcode.com/problems/task-scheduler/description/?envType=company&envId=facebook&favoriteSlug=facebook-all

You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

Return the minimum number of CPU intervals required to complete all tasks.



Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2

Output: 8

Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.

Example 2:

Input: tasks = ["A","C","A","B","D","B"], n = 1

Output: 6

Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

With a cooling interval of 1, you can repeat a task after just one other task.

Example 3:

Input: tasks = ["A","A","A", "B","B","B"], n = 3

Output: 10

Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.



Constraints:

1 <= tasks.length <= 104
tasks[i] is an uppercase English letter.
0 <= n <= 100
"""
from typing import List
import collections
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #
        # "A","A","A", "B","B","B" | n = 3
        #               i
        # {A: 2, B: 3}
        #  A -> B -> [] -> [] -> A -> B ->[] -> [] -> A ->B
        # [(A, 3)]
        counter = collections.Counter(tasks)
        max_heap = [-cnt for cnt in counter.values()]
        heapq.heapify(max_heap) # store the count of each tasks (-1 * count of each task)
        q = collections.deque([]) # (task count, available time)
        time = 0
        while max_heap or q:
            time += 1 # each operation, time will increase by 1
            if max_heap:
                cnt = 1 + heapq.heappop(max_heap) # actually it is cnt of task - 1, means process one task. but because the number in max heap is negative, so use +1 instead of -1
                if cnt < 0:
                    q.append(( cnt, time + n ))
            if q and q[0][1] <= time:
                heapq.heappush(max_heap, (q.popleft()[0]))
        return time
