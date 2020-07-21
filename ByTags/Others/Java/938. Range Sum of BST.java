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
    public int rangeSumBST(TreeNode root, int L, int R) {
        if(root == null){
            return 0;
        }
        if(root.val < L){
            int right = rangeSumBST(root.right, L, R);
            return right;
        }else if(root.val > R){
            int left = rangeSumBST(root.left, L, R);
            return left;
        }else{
            int right = rangeSumBST(root.right, L, R);
            int left = rangeSumBST(root.left, L, R);
            return right + left + root.val;
        }
    }
}