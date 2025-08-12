/**
 * 18. 4Sum
 * https://leetcode.com/problems/4sum/description/
 *
 * Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
 *
 * 0 <= a, b, c, d < n
 * a, b, c, and d are distinct.
 * nums[a] + nums[b] + nums[c] + nums[d] == target
 * You may return the answer in any order.
 *
 *
 *
 * Example 1:
 *
 * Input: nums = [1,0,-1,0,-2,2], target = 0
 * Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
 * Example 2:
 *
 * Input: nums = [2,2,2,2,2], target = 8
 * Output: [[2,2,2,2]]
 *
 *
 * Constraints:
 *
 * 1 <= nums.length <= 200
 * -109 <= nums[i] <= 109
 * -109 <= target <= 109
 */
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */
var fourSum = function(nums, target) {
    nums.sort((a, b) => a - b);
    const ans = [];
    for(let i = 0; i < nums.length; i++) {
        if(i > 0 && nums[i - 1] == nums[i]) continue;
        for(let j = i + 1; j < nums.length; j++) {
            if(j > i + 1 && nums[j] == nums[j - 1]) continue;
            let l = j + 1, r = nums.length - 1;
            while (l < r) {
                let sum = nums[i] + nums[j] + nums[l] + nums[r];
                if (sum === target) {
                    if(l > j + 1 && nums[l] == nums[l - 1]) {
                        l++;
                        continue;
                    }
                    ans.push([nums[i], nums[j], nums[l], nums[r]]);
                    l++;
                    r--;
                } else if(sum > target) r--;
                else l++;
            }
        }
    }
    return ans;
};