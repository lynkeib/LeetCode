/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        return divide(nums, 0, nums.length - 1);
    }

    public TreeNode divide(int[] nums, int start, int end){
        if(start > end){
            return null;
        }
        int maxAt = start;
        for(int i = start; i <= end; i++){
            maxAt = nums[i] > nums[maxAt] ? i : maxAt;
        }
        TreeNode root = new TreeNode(nums[maxAt]);
        root.left = divide(nums, start, maxAt - 1);
        root.right = divide(nums, maxAt + 1, end);
        return root;
    }
}