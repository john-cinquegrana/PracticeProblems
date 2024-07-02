class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Dictionary to store the last known index of the character
        appearance = {}
        # Index of the last known valid character
        start = 0
        # Size of the largest known substring
        size = 0
        # For loop to go over all of the characters
        for i in range(len(s)):
            # Get the current character
            char = s[i]
            if char in appearance and appearance[char] >= start:
                size = max(size, i - start)
                start = appearance[char] + 1
                print(f"Start changed to {start}")
            appearance[char] = i
        # Add the size of the final substring
        size = max(size, len(s) - start)
        
        return size

        
