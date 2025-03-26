"""
1723. https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/description/

You are given an integer array jobs, where jobs[i] is the amount of time it takes to complete the ith job.

There are k workers that you can assign jobs to. Each job should be assigned to exactly one worker. The working time of a worker is the sum of the time it takes to complete all jobs assigned to them. Your goal is to devise an optimal assignment such that the maximum working time of any worker is minimized.

Return the minimum possible maximum working time of any assignment.



Example 1:

Input: jobs = [3,2,3], k = 3
Output: 3
Explanation: By assigning each person one job, the maximum time is 3.
Example 2:

Input: jobs = [1,2,4,7,8], k = 2
Output: 11
Explanation: Assign the jobs the following way:
Worker 1: 1, 2, 8 (working time = 1 + 2 + 8 = 11)
Worker 2: 4, 7 (working time = 4 + 7 = 11)
The maximum working time is 11.


Constraints:

1 <= k <= jobs.length <= 12
1 <= jobs[i] <= 107

"""
from typing import List
class Solution:
    # top down
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        def dfs(i, curr_max_time):  # curr_max_time: max working time to finish i jobs
            nonlocal ans
            if curr_max_time > ans:
                return ans
            if i == len(jobs):
                ans = min(ans, curr_max_time)
                return ans

            time_set = set()
            for j in range(k):
                if w[j] not in time_set:
                    w[j] += jobs[i]
                    ans = min(ans, dfs(i + 1, max(w[j], curr_max_time)))
                    w[j] -= jobs[i]
                    time_set.add(w[j])
            return ans

        ans = float('inf')
        w = [0] * k
        ans = dfs(0, 0)
        return ans

    # bottom up => TLE
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        DIMENION = 2 ** len(jobs)
        dp = [[0] * DIMENION for _ in range(k + 1)]
        time = [0] * DIMENION  # time to finish jobs of state
        n = len(jobs)

        for state in range(1 << n):
            sum = 0
            for i in range(n):
                if (state >> i) & 1:
                    sum += jobs[i]
                time[state] = sum
        for state in range(1, 1 << n):
            dp[0][state] = float('inf')
        dp[0][0] = 0
        for i in range(1, k + 1):
            for state in range(1 << n):
                dp[i][state] = float('inf')
                subset = state
                while subset:
                    dp[i][state] = min(dp[i][state], max(dp[i - 1][state - subset], time[subset]))
                    subset = (subset - 1) & state
        return dp[k][(1 << n) - 1]