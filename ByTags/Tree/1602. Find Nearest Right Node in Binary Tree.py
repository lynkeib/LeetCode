# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def findNearestRightNode(self, root, u):
        """
        :type root: TreeNode
        :type u: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        curr = root
        root.next = None
        while curr:
            dummyhead = TreeNode()
            dummyhead.next = None
            dummytail = dummyhead
            node = curr
            while node:
                if node == u:
                    return node.next
                if node.left:
                    dummytail.next = node.left
                    dummytail = dummytail.next
                if node.right:
                    dummytail.next = node.right
                    dummytail = dummytail.next
                dummytail.next = None
                node = node.next
            curr = dummyhead.next
        return None
