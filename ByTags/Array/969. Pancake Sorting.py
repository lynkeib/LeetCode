class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        res = []
        total = len(arr)
        target = total
        while target > 0:
            # first flip
            index = 0
            while arr[index] != target:
                index += 1
            # does this number need flip?
            if index != target - 1:
                # need first flip?
                if index != 0:
                    self.flip(arr, index)
                    res.append(index + 1)
                # second flip
                res.append(target)
                self.flip(arr, target - 1)
            target -= 1
        return res

    def flip(self, arr, index):
        left, right = 0, index
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return