from math import floor, ceil

class Solution:
    def reverse(self, x: int) -> int:
        # Constants to help handle the constraints
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        pos_limit = MAX_INT // 10
        neg_limit = ceil(MIN_INT / 10)
        
        # Helper functions to test limit
        def can_increase(num, digit):
            if num > pos_limit:
                return False
            elif num == pos_limit:
                # 7 is the ones column of the MAX_INT
                return digit <= 7
            else:
                return True
        # Helper function to determine if the number is too small
        def can_decrease(num, digit):
            if num < neg_limit:
                return False
            elif num == neg_limit:
                # -8 is the ones column of the MIN_INT
                return digit >= -8
            else:
                return True

        # The result we will return
        result = 0

        # Remember, in the bits, 0 is considered a positive integer
        is_positive = x >= 0
        div_adj = 0 if is_positive else 1

        # Loop over the number
        while (is_positive and x > 0) or x < 0:
            # Pull the digit and decrement x
            digit = x % 10
            x = (x / 10)

            if is_positive:
                # Edit x
                x = floor(x)
                # Test to see if we can increase
                if not can_increase(result, digit):
                    print("Exit out of positive")
                    return 0
            else:
                x = ceil(x)
                # Edit the digit because we hate mod
                digit = digit - 10 if digit > 0 else 0
                # Test for size
                if not can_decrease(result, digit):
                    print("Exit out of negative")
                    return 0

            # Increment the result and add this digit
            result *= 10
            result += digit
            # print(result)
        # End of while loop

        # Return our result
        return result
