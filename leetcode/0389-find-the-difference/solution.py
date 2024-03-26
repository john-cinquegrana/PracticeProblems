class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # s is the original string
        # t is the shuffled and added string

        # Create a dictionary to store the number of occurences of each character
        char_dict = {}
        for char in s:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1

        # Iterate through the shuffled string and decrement the count of each character
        for char in t:
            if char in char_dict:
                char_dict[char] -= 1
                if char_dict[char] < 0:
                    return char
            else:
                return char
