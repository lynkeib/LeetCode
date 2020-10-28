class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        for f in path.split("/"):
            if f == "." or f == "":
                continue
            elif f == "..":
                if stack: stack.pop()
            else:
                stack.append(f)
        return "/" + "/".join(stack)