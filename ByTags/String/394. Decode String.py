class Solution(object):
    index = 0

    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        while self.index < len(s) and s[self.index] != "]":
            if s[self.index].isnumeric():
                num = 0
                while self.index < len(s) and s[self.index].isnumeric():
                    num = num * 10 + int(s[self.index])
                    self.index += 1

                self.index += 1  # skip "["
                rest = self.decodeString(s)
                self.index += 1  # skip "]"

                res += rest * num
            else:
                res += s[self.index]
                self.index += 1
        return res
