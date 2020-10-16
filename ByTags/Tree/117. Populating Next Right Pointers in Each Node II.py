"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return
        curr = root
        while curr:
            dummyhead = Node()
            dummytail = dummyhead
            node = curr
            while node:
                if node.left:
                    dummytail.next = node.left
                    dummytail = dummytail.next
                if node.right:
                    dummytail.next = node.right
                    dummytail = dummytail.next
                node = node.next
            curr = dummyhead.next
        return root