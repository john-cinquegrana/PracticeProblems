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
    
    def is_empty(self):
        return self.peek is None