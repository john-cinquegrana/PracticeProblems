class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Make the pattern list into an array of patterns to be easier to
        #handle
        patterns = []
        i = 0
        while i < len(p):
            if i+1 < len(p) and p[i+1]=='*':
                patterns.append( p[i:i+2] )
                i += 2
            else:
                patterns.append(p[i])
                i += 1
        # Build the DP matrix for memoization, indexed first by string
        # character, then by pattern item
        mat = [ [False for i in range(len(patterns)+1)] for i in range(len(s)+1) ]

        # Put a true for the 0, 0 location
        mat[0][0] = True

        # Fill up the no pattern, but with string spots, with falses
        # for s_i in range(1, len(s)):
        #     mat[s_i][0] = False

        # Fill up the first patterns as well
        for p_i in range(1, len(patterns)):
            # We only care if it's a star
            patt = patterns[p_i-1]
            mat[0][p_i] = mat[0][p_i-1] and ('*' in patt)

        # The main iteration over the matrix
        for s_i in range(1, len(s)+1):
            for p_i in range(1, len(patterns)+1):
                # Get the pattern and character
                char = s[s_i-1]
                patt = patterns[p_i-1]

                # This will be true if this pattern matches the current
                # character
                matched = '.' in patt or char in patt

                # If we have a star, we're always true if the left is true
                if '*' in patt:
                    mat[s_i][p_i] = mat[s_i][p_i-1] or (matched and (mat[s_i-1][p_i-1] or mat[s_i-1][p_i]))
                # If no star, we're true if this pattern can consume this character
                else:
                    mat[s_i][p_i] = mat[s_i-1][p_i-1] and matched

        # Print out the matrix
        # print(mat)

        # Return true if the final character pair returns true
        return mat[-1][-1]
