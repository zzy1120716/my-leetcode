"""
155. Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in
constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_val = float('inf')

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if x <= self.min_val:
            self.stack.append(self.min_val)
            self.min_val = x
        self.stack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if self.stack.pop() == self.min_val:
            self.min_val = self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_val


if __name__ == '__main__':
    # Your MinStack object will be instantiated and called as such:
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    obj.pop()
    print(obj.top())
    print(obj.getMin())
