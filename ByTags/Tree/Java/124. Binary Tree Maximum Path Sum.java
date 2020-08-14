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
    int res = Integer.MIN_VALUE;
    public int maxPathSum(TreeNode root) {
        helper(root);
        return res;
    }

    public int helper(TreeNode root){
        if(root == null){
            return 0;
        }
        var left = helper(root.left);
        var right = helper(root.right);
        left = left < 0 ? 0 : left;
        right = right < 0 ? 0 : right;
        var thisMaxV = left + right + root.val;
        var thisMax = (left < right ? right : left) + root.val;
        res = Math.max(res, thisMax);
        res = Math.max(res, thisMaxV);
        return thisMax;
    }
}