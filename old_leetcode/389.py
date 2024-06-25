'''
File:			389.py
Project:		Practice Problems
File Created:	Thursday, January 1st 1970
Remote:			PracticeProblems at 'https://github.com/john-cinquegrana/PracticeProblems'
Author(s):		John Cinquegrana (alllegron@gmail.com)

Copyright 2024 John Cinquegrana (alllegron@gmail.com)

https://leetcode.com/problems/find-the-difference/
'''

__author__		=	"John Cinquegrana"
__copyright__	=	"Copyright 2024 John Cinquegrana (alllegron@gmail.com)"

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