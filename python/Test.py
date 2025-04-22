from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        #     i.
        # -4,-1,1,2     sum = -1 + 1 + 2 = 2 < 1 , min_diff = 1 -(2) = -1, 2
        #       l
        #         r
        sum = 0
        min_diff = float('inf')
        ans = float('inf')
        nums.sort()
        for i in range(len(nums) - 2):
            print(i)
            if i > 0 and nums[i] == nums[i - 1]: continue
            l, r = i + 1, len(nums) - 1
            print(i, l, r)
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == target:
                    return sum
                else:
                    print(sum)
                    if abs(sum - target) < min_diff:
                        min_diff = abs(sum - target)
                        ans = sum
                    if sum < target:
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    else:
                        r -= 1
            return ans


nums = [-1,2,1,-4]
Solution().threeSumClosest(nums, 1)