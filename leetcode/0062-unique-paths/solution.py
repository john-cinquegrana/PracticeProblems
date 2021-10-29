class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # Create a matrix of all zeroes to represent the unique paths
        # We have padding so we don't have to deal with border detection
        matrix = [ [0 for i in range(n+1)] for j in range(m+1) ]
        
        
        # This is a hack to get a 1 in the square at 1,1
        matrix[0][1] = 1
        # print(matrix)
        
        for row in range(1, m+1):
            for col in range(1, n+1):
                # We progress first left to right, then top to bottom across the matrix
                # From the cells directly above and to the left, there is one way to get to this cell
                #       therefore we simply add them together
                matrix[row][col] = matrix[row-1][col] + matrix[row][col-1]
        
        # print(matrix)
        return matrix[-1][-1]
                
        
