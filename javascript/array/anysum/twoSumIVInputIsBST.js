/**
 *  653. Two Sum IV - Input is a BST
 *  https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/
 *
 *  Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.
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
import TreeNode from '../../model/treenode.js';
var findTarget = function(root, k) {
    const nums = [];
    dfs(root, nums);
    let l = 0, r = nums.length - 1;
    while ( l < r) {
        let sum = nums[l] + nums[r];
        if (sum == k) return true;
        else if (sum > k) r--;
        else l++;
    }
    return false;
};

var dfs = function(node, nums) {
    if (node == null) return;
    dfs(node.left, nums);
    nums.push(node.val);
    dfs(node.right, nums);
}

// const obj = {tree: TreeNode};
// const node = obj.tree(1);
const root = { }
TreeNode.call(root, 1, null, null)
const left = {}
TreeNode.call(left, 0, null, null)
root.left = left;
// tree.left = TreeNode(0);
console.log(findTarget(root, 1));