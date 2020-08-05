/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
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
    public TreeNode sortedListToBST(ListNode head) {
        return buildTree(head);
    }

    public TreeNode buildTree(ListNode head){
        if(head == null){
            return null;
        }
        ListNode prev = null, slow = head, fast = head;
        while(fast.next != null && fast.next.next != null){
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        if(slow == head){
            TreeNode node = new TreeNode(slow.val);
            if(slow.next != null){
                TreeNode t_node = new TreeNode(slow.next.val);
                t_node.left = node;
                return t_node;
            }else{
                return node;
            }
        }

        prev.next = null;
        TreeNode node = new TreeNode(slow.val);
        node.left = buildTree(head);
        node.right = buildTree(slow.next);
        return node;
    }
}