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
