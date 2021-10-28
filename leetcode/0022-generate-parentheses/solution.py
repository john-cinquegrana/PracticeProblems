class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        def generate(word, lefts, rights):
            if lefts == n and rights == n:
                result.append("".join(word))
            else:
                if lefts < n:
                    # We have room for another pair
                    word.append("(")
                    generate(word, lefts+1, rights)
                    word.pop() # Remove the paren to keep backtracking
                if rights < lefts:
                    # We can close a pair
                    word.append(")")
                    generate(word, lefts, rights+1)
                    word.pop() # Remove the paren to keep backtracking
        # End of generate function
        generate([], 0, 0)
        # 'result' variable is now populated
        return result
                
