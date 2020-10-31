# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        c = self.dfs(head)
        if c:
            newHead = ListNode(c)
            newHead.next = head
            head = newHead
        return head

    def dfs(self, node):
        if not node.next:
            val = node.val
            s = 1 + val
            node.val = s % 10
            return s // 10
        carry = self.dfs(node.next)
        val = node.val
        s = carry + val
        node.val = s % 10
        return s // 10