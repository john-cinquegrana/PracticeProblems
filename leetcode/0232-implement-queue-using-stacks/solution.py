class Stack:
    def __init__(self):
        self.ls = []

    def push(self, x: int):
        self.ls.append(x)

    def peek(self):
        if self.ls:
            return self.ls[-1]
        else:
            return None

    def pop(self):
        return self.ls.pop()

class MyQueue:

    def __init__(self):
        ''' The plan is to use the queueStack as a representation of the queue.
        At any point between function calls, queueStack should be in the
        correct order of a queue. The workStack will be used to help keep the
        queueStack in proper order during function calls.'''
        self.queueStack = Stack()
        self.workStack = Stack()

    def push(self, x: int) -> None:
        # Reverse the queueStack onto the workStack
        while self.queueStack.peek() is not None:
            self.workStack.push( self.queueStack.pop() )
        # Push our good item onto the queue stack
        self.queueStack.push(x)
        # Re-reverse the items onto the queueStack again, this time on top of
        # the added element.
        while self.workStack.peek() is not None:
            self.queueStack.push( self.workStack.pop() )

    def pop(self) -> int:
        return self.queueStack.pop()

    def peek(self) -> int:
        return self.queueStack.peek()        

    def empty(self) -> bool:
        return self.queueStack.peek() is None
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
