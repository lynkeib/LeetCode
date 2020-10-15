class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        len1, len2 = len(num1), len(num2)
        num1 = num1[::-1]
        num2 = num2[::-1]
        res = [0] * (len1 + len2)
        for index1 in range(len1):
            n1 = int(num1[index1])
            for index2 in range(len2):
                n2 = int(num2[index2])
                thisProduct = n1 * n2
                low = thisProduct % 10
                high = thisProduct // 10
                res[index1 + index2] += low
                res[index1 + index2 + 1] += high
        for i in range(len(res) - 1):
            if res[i] >= 10:
                upper = res[i] // 10
                res[i] = res[i] % 10
                res[i + 1] += upper
        s = ""
        for i in range(len(res) - 1, -1, -1):
            if res[i] == 0 and not s:
                continue
            s += str(res[i])
        return s if s else "0"