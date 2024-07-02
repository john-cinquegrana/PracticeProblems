class Solution:
    def myAtoi(self, s: str) -> int:
        # pointer for our index
        index = 0

        # Go past all whitespace
        while index < len(s) and s[index].isspace():
            index += 1

        if index >= len(s):
            return 0

        # Determine the sign
        is_positive = False
        match s[index]:
            case '-':
                is_positive = False
                index += 1
            case '+':
                is_positive = True
                index += 1
            case _:
                is_positive = True
                # Don't advance the pointer because we are assuming the sign
        
        # Loop until we get to something interesting
        while index < len(s) and s[index] == '0':
            index += 1
        
        # Find the end of the number
        end_index = index
        while end_index < len(s) and s[end_index].isdigit():
            end_index += 1

        # Get the substring we are interested in
        number_string = s[index : end_index]

        # Make sure this list exists
        if not number_string:
            return 0
        
        # Convert the string to a number
        number = int(number_string)

        # Make negative if necessary
        if not is_positive:
            number *= -1

        # Round the number if necessary
        if number > (2**31 - 1):
            number = 2**31 - 1
        elif number < -2 ** 31:
            number = -2 ** 31

        return number
