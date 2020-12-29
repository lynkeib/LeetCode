class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.next = nextNode


class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.capacity = k
        self.head = None
        self.tail = None
        self.count = 0

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.count == self.capacity:
            return False

        if self.count == 0:
            self.head = Node(value)
            self.tail = self.head
        else:
            n = Node(value)
            self.tail.next = n
            self.tail = n
        self.count += 1
        return True

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.count == 0:
            return False
        self.head = self.head.next
        self.count -= 1
        return True

    def Front(self):
        """
        :rtype: int
        """
        if self.count == 0:
            return -1
        return self.head.value

    def Rear(self):
        """
        :rtype: int
        """
        if self.count == 0:
            return -1
        return self.tail.value

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.count == 0

    def isFull(self):
        """
        :rtype: bool
        """
        return self.count == self.capacity

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()