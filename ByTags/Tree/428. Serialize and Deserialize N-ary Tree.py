"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Codec:
    unicode_num = 37

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        if not root:
            return
        queue = [root, None]
        res = []
        while queue:
            thisNode = queue.pop(0)
            if not thisNode:
                res.append("#")
                if queue:
                    queue.append(None)
            elif thisNode == "C":
                res.append("$")
            else:
                res.append(chr(thisNode.val + self.unicode_num))
                for child in thisNode.children:
                    queue.append(child)
                if queue[0] != None:
                    queue.append("C")
        return "".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        if not data:
            return
        root = Node(ord(data[0]) - self.unicode_num, [])
        prevLevel, currLevel = [], [root]
        currParnet = root
        for i in range(1, len(data)):
            thisChar = data[i]
            if thisChar == "#":
                prevLevel = currLevel
                currLevel = []
                currParnet = prevLevel.pop(0) if prevLevel else None
            elif thisChar == "$":
                currParnet = prevLevel.pop(0) if prevLevel else None
            else:
                thisNode = Node(ord(thisChar) - self.unicode_num, [])
                currLevel.append(thisNode)
                currParnet.children.append(thisNode)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))