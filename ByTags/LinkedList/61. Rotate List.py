# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return
        totel_length = 0
        curr = head
        while curr:
            curr = curr.next
            totel_length += 1
        k %= totel_length
        if k == 0:
            return head
        k = totel_length - k
        dummyhead = ListNode()
        dummyhead.next = head
        prev, curr = dummyhead, head
        while k > 0:
            prev = curr
            curr = curr.next
            k -= 1
        prev.next = None
        dummyhead.next = curr
        while curr.next:
            curr = curr.next
        curr.next = head
        return dummyhead.next