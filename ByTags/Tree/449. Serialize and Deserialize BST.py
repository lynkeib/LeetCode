# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []
        curr = root
        stack = []
        while curr or stack:
            while curr:
                stack.append(curr)
                res.append(str(curr.val))
                curr = curr.right
            curr = stack.pop()
            curr = curr.left
        return ";".join(res[::-1])

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = list(map(int, data.split(";")))
        self.i = len(data) - 1

        def helper(left, right):
            if self.i < 0 or data[self.i] < left or data[self.i] > right:
                return None
            node = TreeNode(data[self.i])
            self.i -= 1
            node.right = helper(node.val, right)
            node.left = helper(left, node.val)
            return node

        return helper(-float("inf"), float("inf"))

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans