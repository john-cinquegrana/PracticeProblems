'''
File:			455.py
Project:		Practice Problems
File Created:	Thursday, January 1st 1970
Remote:			PracticeProblems at 'https://github.com/john-cinquegrana/PracticeProblems'
Author(s):		John Cinquegrana (alllegron@gmail.com)

Copyright 2024 John Cinquegrana (alllegron@gmail.com)

https://leetcode.com/problems/assign-cookies/
'''

__author__		=	"John Cinquegrana"
__copyright__	=	"Copyright 2024 John Cinquegrana (alllegron@gmail.com)"

from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        sorted_greed = sorted(g)
        sorted_cookies = sorted(s)

        cookie_index = len(s) - 1
        greed_index = len(g) - 1

        cookie_sum = 0

        while (cookie_index >= 0 and greed_index >= 0):
            if sorted_cookies[cookie_index] >= sorted_greed[greed_index]:
                cookie_index -= 1
                cookie_sum += 1
            greed_index -= 1

        return cookie_sum