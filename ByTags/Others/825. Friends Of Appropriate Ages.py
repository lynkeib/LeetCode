class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        counter = dict()
        for age in ages:
            if age not in counter:
                counter[age] = 0
            counter[age] += 1

        res = 0
        for key, value in counter.items():
            for otherAge in counter:
                if 0.5 * key + 7 < otherAge and key >= otherAge and (key >= 100 or otherAge <= 100):
                    res += value * counter[otherAge]
                    if key == otherAge:
                        res -= value
        return res

word = "1234"
Tier = {}
node = Tier
for letter in word:
    node = node.setdefault(letter, {})
print(Tier)