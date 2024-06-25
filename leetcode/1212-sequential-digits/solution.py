
class Expanded:
    # Least significant digits ar at the higher indices
    def __init__(self, x: int):
        self.ls = []
        while x > 0:
            self.ls.append(x % 10)
            x = x // 10
        self.ls.reverse()

    def __gt__(self, other):
        # Check to see if the lengths are different
        if len(self.ls) > len(other.ls):
            return True
        elif len(other.ls) > len(self.ls):
            return False
        # We know that the lengths are equal
        length = len(self.ls)
        for i in range(length):
            if self.ls[i] > other.ls[i]:
                return True
            elif self.ls[i] < other.ls[i]:
                return False
        # They are the same number
        return False

    def __le__(self, other):
        # Check to see if the lengths are different
        if len(self.ls) < len(other.ls):
            return True
        elif len(other.ls) > len(self.ls):
            return False
        # We know that the lengths are equal
        length = len(self.ls)
        for i in range(length):
            if self.ls[i] < other.ls[i]:
                return True
            elif self.ls[i] > other.ls[i]:
                return False
        # They are the same number
        return True

    def to_number(self):
        result = 0
        for num in self.ls:
            result *= 10
            result += num
        return result

    def make_sequential(self):
        last = self.ls[0] - 1
        i = 0
        upscaled = False
        while i < len(self.ls):
            print(f"i: {i}, last: {last}, ls: {self.ls}")
            # Make sure we are increasing
            if self.ls[i] <= last:
                self.ls[i] = last + 1
                upscaled = True
            elif self.ls[i] > last + 1 and not upscaled:
                self.ls[i-1] += 1
                for j in range(i, len(self.ls)):
                    self.ls[j] = 0
                i = 0
                last = self.ls[0] - 1
                continue
            elif self.ls[i] > last + 1 and upscaled:
                self.ls[i] = last + 1
            
            last = self.ls[i]
            # Make sure the number is small enough in total
            max_value = 10 - len(self.ls) + i
            if max_value <= 0:
                return
            if (self.ls[i] > max_value):
                # We need to add a new digit
                self.ls.insert(0, 1)
                # zero out the rest of the number
                for i in range(1, len(self.ls)):
                    self.ls[i] = 0
                # Restart the loop
                last = 0
                i = 0
            else:
                i += 1

    def increment(self, amount=1):
        make_mark = False
        for i in range(0, len(self.ls)):
            self.ls[i] += amount
            if self.ls[i] >= 10:
                make_mark = True
        if make_mark:
            self.make_sequential()


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # Set up the guys in expanded form
        low = Expanded(low)
        high = Expanded(high)
        top = Expanded(10**9)

        # Coersce the low into the lowest sequential number greater than itself.
        low.make_sequential()

        result = []

        while low <= high and low < top:
            num = low.to_number()
            print(f"adding {num} to list")
            result.append(num)
            low.increment()

        return result
    
