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

    Map<Integer, Integer> presum = new HashMap<>();

    public int pathSum(TreeNode root, int sum) {
        presum.put(0, 1);
        return helper(root, sum, 0);
    }

    private int helper(TreeNode root, int sum, int currSum) {
        if (root == null){
            return 0;
        }

        currSum += root.val;
        int target = currSum - sum;
        int res = presum.getOrDefault(target, 0);
        presum.put(currSum, presum.getOrDefault(currSum, 0) + 1);

        res += helper(root.left, sum, currSum);
        res += helper(root.right, sum, currSum);
        presum.put(currSum, presum.get(currSum) - 1);

        return res;
    }
}
