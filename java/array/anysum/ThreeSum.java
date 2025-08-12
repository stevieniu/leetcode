package array.anysum;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ThreeSum {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        var ans = new ArrayList<List<Integer>>();

        for (int i = 0; i < nums.length; i++) {
            if(i > 0 && nums[i] == nums[i - 1]) continue;
            int j = i + 1, k = nums.length - 1;
            while (j < k) {
                int sum = nums[i] + nums[j] + nums[k];
                if(sum == 0) {
                    if (j > i + 1 && nums[j] == nums[j - 1]) {
                        j++;
                        continue;
                    }
                    ans.add(Arrays.asList(nums[i], nums[j], nums[k]));
                    j++;
                    k--;
                } else if (sum > 0) k--;
                else j++;
            }
        }
        return ans;
    }
}
