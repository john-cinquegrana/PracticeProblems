from math import floor, log10

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Return false if we're negative
        if x < 0:
            return False
        elif x == 0:
            return True
        # Get the number of digits of the number
        digits = floor( log10(x)+1 )
        halfway = digits // 2
        odd_digits = (digits % 2) == 1
        # Create the stack to push numbers onto
        stack = []
        # For half the number, push digits onto the stack
        for i in range(halfway):
            it = x % 10
            x //= 10
            stack.append(it)
        # If we have an odd number of digits, we get rid of one more
        if odd_digits:
            x //= 10
        # Match the second half of the number
        while x > 0:
            it = x % 10
            x //= 10
            if it != stack.pop():
                return False
        return True
