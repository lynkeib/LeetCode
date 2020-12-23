# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        inorder = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            inorder.append(curr.val)
            curr = curr.right
        root = self.build(inorder, 0, len(inorder) - 1)
        return root

    def build(self, inorder, start, end):
        if start > end:
            return None
        mid = start + (end - start) / 2
        root = TreeNode(inorder[mid])
        root.left = self.build(inorder, start, mid - 1)
        root.right = self.build(inorder, mid + 1, end)
        return root


