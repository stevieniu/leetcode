/**
 * 653. Two Sum IV - Input is a BST
 * https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/
 *
 * Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.
 *
 *
 *
 * Example 1:
 *
 *
 * Input: root = [5,3,6,2,4,null,7], k = 9
 * Output: true
 * Example 2:
 *
 *
 * Input: root = [5,3,6,2,4,null,7], k = 28
 * Output: false
 *
 *
 * Constraints:
 *
 * The number of nodes in the tree is in the range [1, 104].
 * -104 <= Node.val <= 104
 * root is guaranteed to be a valid binary search tree.
 * -105 <= k <= 105
 */
package array.anysum;

import model.TreeNode;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class TwoSumIVInputIsABST {
    List<Integer> nums;
    public boolean findTarget_1 (TreeNode root, int k) {
        nums = new ArrayList<>();
        dfs(root);
        int l = 0, r = nums.size() - 1;
        while (l < r) {
            int sum = nums.get(l) + nums.get(r);
            if (sum == k) return true;
            else if (sum > k) r--;
            else l++;
        }
        return false;
    }
    public void dfs(TreeNode node) {
        if (node == null) return;
        dfs(node.left);
        nums.add(node.val);
        dfs(node.right);
    }


    Set<Integer> dataSet;
    public boolean findTarget_2(TreeNode root, int k) {
        dataSet = new HashSet<>();
        return dfs(root, k);
    }

    public boolean dfs(TreeNode node, int k) {
        if (node == null) return false;
        if (dataSet.contains(k - node.val)) return true;
        dataSet.add(node.val);
        return dfs(node.left, k) || dfs(node.right, k);
    }
}
