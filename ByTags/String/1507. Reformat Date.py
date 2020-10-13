class Solution(object):
    def reformatDate(self, date):
        """
        :type date: str
        :rtype: str
        """
        month = {
            "Jan": "01",
            "Feb": "02",
            "Mar": "03",
            "Apr": "04",
            "May": "05",
            "Jun": "06",
            "Jul": "07",
            "Aug": "08",
            "Sep": "09",
            "Oct": "10",
            "Nov": "11",
            "Dec": "12"
        }
        d = date.split(" ")
        res = []
        res += [d[2]]
        res += [month[d[1]]]
        res += ["{:02d}".format(int(d[0][:-2]))]
        return "-".join(res)
print([1,2,3] * 3)

