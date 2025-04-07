from typing import List
def threeSum(nums: List[int]) -> List[List[int]]:
    # i
    # -4 -1 -1 0 1 2
    #     l        
    #              r     nums[r] + nums[l] == -nums[i]
    if not nums: return []
    nums.sort()
    ans = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]: continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            if nums[i] + nums[l] + nums[r] == 0:
                ans.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
            elif nums[i] + nums[l] + nums[r] < 0:
                r -= 1
            else:
                l += 1
    return ans

nums = [1,-1,-1,0]
print(threeSum(nums))