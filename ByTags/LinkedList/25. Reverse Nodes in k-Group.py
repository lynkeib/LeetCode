# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k <= 1:
            return head
        dummyhead = ListNode(0, head)
        start = dummyhead

        while 1:
            count = k
            curr = start

            while curr and count > 0:
                curr = curr.next
                count -= 1

            if not curr:
                return dummyhead.next

            ## reverse
            count = k
            prevNode = None
            nextNode = start.next
            while count:
                t = nextNode.next
                nextNode.next = prevNode
                prevNode = nextNode
                nextNode = t
                count -= 1
            temp = start.next
            start.next = prevNode
            temp.next = nextNode
            start = temp

        return dummyhead.next
