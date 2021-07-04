class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.items.append(val)

    def pop(self):
        """
        :rtype: None
        """
        return self.items.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.items[len(self.items)-1]

    def getMin(self):
        """
        :rtype: int
        """
        m = self.items[0]
        for item in self.items[1:] : 
            if m > item :
                m = item
        return m


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
