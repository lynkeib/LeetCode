class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                continue

            slow, fast = i, self.getIndex(i, nums)
            while nums[slow] * nums[fast] > 0 and nums[slow] * nums[self.getIndex(fast, nums)] > 0:
                if slow == fast:
                    if fast == self.getIndex(fast, nums):
                        break
                    return True
                slow = self.getIndex(slow, nums)
                fast = self.getIndex(self.getIndex(fast, nums), nums)
            slow = i
            thisVal = nums[slow]
            while nums[slow] * thisVal > 0:
                nextSlow = self.getIndex(slow, nums)
                nums[slow] = 0
                slow = nextSlow
        return False

    def getIndex(self, index, nums):
        return (index + nums[index]) % len(nums)



def circular_array_loop_exists(arr):
    for i in range(len(arr)):
        is_forward = arr[i] >= 0  # if we are moving forward or not
        slow, fast = i, i

        # if slow or fast becomes '-1' this means we can't find cycle for this number
        while True:
            # move one step for slow pointer
            slow = find_next_index(arr, is_forward, slow)
            # move one step for fast pointer
            fast = find_next_index(arr, is_forward, fast)
            if (fast != -1):
                # move another step for fast pointer
                fast = find_next_index(arr, is_forward, fast)
            if slow == -1 or fast == -1 or slow == fast:
                break

        if slow != -1 and slow == fast:
            return True

    return False


def find_next_index(arr, is_forward, current_index):
    direction = arr[current_index] >= 0

    if is_forward != direction:
        return -1  # change in direction, return -1

    next_index = (current_index + arr[current_index]) % len(arr)

    # one element cycle, return -1
    if next_index == current_index:
        next_index = -1

    return
