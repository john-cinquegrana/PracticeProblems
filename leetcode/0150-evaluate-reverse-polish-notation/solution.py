
from math import floor, ceil

class Solution:
    def round(self, x) -> int:
        if x > 0:
            return floor(x)
        else: return ceil(x)

    def evalRPN(self, tokens: List[str]) -> int:
        # Declare the stack that we'll be working with
        stack = []
        # Iterate through the list, putting operands on the stack until we hit
        # an operator
        for char in tokens:
            match char:
                case '+':
                    stack.append( stack.pop() + stack.pop() )
                case '-':
                    stack.append( -1 * stack.pop() + stack.pop())
                case '/':
                    stack.append(self.round(
                        1 / stack.pop() * stack.pop()
                    ))
                case '*':
                    stack.append(stack.pop() * stack.pop())
                case _:
                    stack.append(int(char))
        return stack.pop()
