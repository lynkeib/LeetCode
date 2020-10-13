# iterative:
class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        counter = dict()
        item = ""
        stack = []
        count, numberCount = 0, 0
        currCount = 1

        for c in formula[::-1]:
            if c.isnumeric():
                count += int(c) * (10 ** numberCount)
                numberCount += 1
            elif c == ")":
                stack.append((count or 1))
                currCount *= count
                count = 0
                numberCount = 0
            elif c == "(":
                currCount //= stack.pop()
                count = 0
                numberCount = 0
            elif c.isupper():
                item += c
                thisItem = item[::-1]
                if thisItem not in counter:
                    counter[thisItem] = 0
                counter[thisItem] += (count or 1) * currCount
                item = ""
                count = 0
                numberCount = 0
            elif c.islower():
                item += c

        res = ""
        for key, value in sorted(counter.items()):
            if value > 1:
                res += key + str(value)
            else:
                res += key
        return res


# recursive: TLE
class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        res = self.helper(formula, 0)
        lst = res[0]
        counter = collections.Counter(lst)
        res = ""
        keys = sorted(counter.keys())
        for item in keys:
            res += item
            res += str(counter[item]) if counter[item] != 1 else ""
        return res

    def helper(self, s, index):
        res = []
        if index == len(s):
            return res, index
        curr = []
        i = index
        while i < len(s):
            c = s[i]
            if c == ")":
                if curr:
                    res += curr
                    curr = []
                i += 1
                num = 0
                while i < len(s) and s[i].isnumeric():
                    num = num * 10 + int(s[i])
                    i += 1
                return res * num, i
            elif c == "(":
                if curr:
                    res += curr
                    curr = []
                temp = self.helper(s, i + 1)
                res += temp[0]
                i = temp[1]
                if i == len(s):
                    return res, len(s)
                i -= 1
            elif c.isupper():
                item = c
                i += 1
                while i < len(s) and s[i].islower():
                    item += s[i]
                    i += 1
                curr.append(item)
                i -= 1
            elif c.isnumeric():
                num = 0
                while i < len(s) and s[i].isnumeric():
                    num = num * 10 + int(s[i])
                    i += 1
                res += curr
                res += [curr[-1]] * (num - 1)
                curr = []
                i -= 1
            i += 1
        return res + curr, len(s)