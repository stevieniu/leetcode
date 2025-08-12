/**
 * 560. Subarray Sum Equals K
 * https://leetcode.com/problems/subarray-sum-equals-k/description/
 *
 * Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
 *
 * A subarray is a contiguous non-empty sequence of elements within an array.
 *
 *
 *
 * Example 1:
 *
 * Input: nums = [1,1,1], k = 2
 * Output: 2
 * Example 2:
 *
 * Input: nums = [1,2,3], k = 3
 * Output: 2
 *
 *
 * Constraints:
 *
 * 1 <= nums.length <= 2 * 104
 * -1000 <= nums[i] <= 1000
 * -107 <= k <= 107
 */
package hashmap.prefixsum;

import java.util.HashMap;

public class SubarraySumEqualsK {
    public int subarraySum(int[] nums, int k) {
        var prefixSumCache = new HashMap<Integer, Integer>();
        prefixSumCache.put(0, 1);
        int ans = 0;
        int prefixSum = 0;
        for(int d : nums) {
            prefixSum += d;
            ans += prefixSumCache.getOrDefault(prefixSum - k, 0);
            prefixSumCache.put(prefixSum, prefixSumCache.getOrDefault(prefixSum, 0) + 1);
        }
        return ans;
    }
}
