class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # If there's only one row, return immediately
        if numRows == 1:
            return s
        # Create the list of characters that will be our result
        chars = []

        # Include the step length, every pattern takes (numRows*2)-2 characters
        # to print out
        step_size = numRows*2 - 2
        # The first row has no duplicates, it gets it's own list
        for i in range(0, len(s), step_size):
            chars.append(s[i])
        # All rows except the first and last get two characters in them per
        # diagonal and belong to this loop
        for row in range(1, numRows-1):
            for i in range(0, len(s), step_size):
                first_index = i + row
                second_index = i + step_size - row
                # Check to make sure they're in range before accessing
                if first_index < len(s):
                    chars.append(s[first_index])
                if second_index < len(s):
                    chars.append(s[second_index])
        # The last row also has no duplicates, so we run it alone
        for i in range(0, len(s), step_size):
            index = i + numRows-1
            if index < len(s):
                chars.append(s[index])

        # Return the string we have built
        return "".join(chars)

        
